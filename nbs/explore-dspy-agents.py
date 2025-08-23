import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _(dspy):
    def evaluate_math(expression: str):
        return dspy.PythonInterpreter({}).execute(expression)

    def search_wikipedia(query: str):
        results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(query, k=3)
        return [x["text"] for x in results]

    react = dspy.ReAct("question -> answer: float", tools=[evaluate_math, search_wikipedia])

    pred = react(question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?")
    print(pred.answer)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Setup""")
    return


@app.cell
def _():
    import os

    import marimo as mo
    from dotenv import load_dotenv
    from openai import OpenAI

    import dspy

    assert load_dotenv(), "Failed to load .env file"

    MODEL = "Qwen/Qwen2.5-3B-Instruct"

    openai_client = OpenAI()

    lm = dspy.LM(
        f"openai/{MODEL}",
        api_base=os.getenv("OPENAI_API_BASE"),
        api_key=os.getenv("OPENAI_API_KEY"),
        model_type="chat",
    )
    dspy.configure(lm=lm)

    return dspy, lm, mo


@app.cell
def _():
    import mlflow
    # Tell MLflow about the server URI.
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.autolog()
    # Create a unique name for your experiment.
    mlflow.set_experiment("DSPy")
    return


@app.cell
def _(lm):
    lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']
    return


@app.cell
def _(lm):
    lm(messages=[{"role": "user", "content": "Say this is a test!"}])  # => ['This is a test!']
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
