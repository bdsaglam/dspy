#!/bin/bash

SESSION="dspy"

# Start new session, but don't attach
tmux new-session -d -s $SESSION

# Window 0: vLLM server
tmux rename-window -t $SESSION:0 'vllm'
tmux send-keys -t $SESSION:0 'CUDA_VISIBLE_DEVICES=0 uvx --python 3.11 --from vllm vllm serve Qwen/Qwen2.5-3B-Instruct --dtype auto --max-model-len 32768 --enable-auto-tool-choice --tool-call-parser hermes --api-key something' C-m
sleep 1

# Window 1: MLflow shell
tmux new-window -t $SESSION:1 -n 'mlflow'
tmux send-keys -t $SESSION:1 'mlflow server --backend-store-uri sqlite:///tmp/mlflow.sqlite' C-m
sleep 1

# Window 2: marimo shell
tmux new-window -t $SESSION:2 -n 'marimo'
tmux send-keys -t $SESSION:2 'marimo edit' C-m
sleep 1

# Window 3: bash shell
tmux new-window -t $SESSION:3 -n 'bash'

# Make sure we're on the vllm window and attach
tmux select-window -t $SESSION:0
tmux attach-session -t $SESSION