## vllm

```sh
CUDA_VISIBLE_DEVICES=0 uvx --python 3.11 --from vllm vllm serve Qwen/Qwen2.5-3B-Instruct \
  --dtype auto \
  --max-model-len 32768 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --api-key something
```


## MLflow

```sh
uv add --dev mlflow>=2.18.0 
```


```sh
mlflow server --backend-store-uri sqlite:///tmp/mlflow.sqlite
```


```py
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("DSPy")
```



