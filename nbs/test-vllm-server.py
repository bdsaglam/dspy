import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _(openai_client):
    openai_client.models.list()
    return


@app.cell
def _(MODEL, openai_client):
    completion = openai_client.completions.create(
        model=MODEL,
        prompt="San Francisco is a",
    )
    completion
    return


@app.cell
def _(MODEL, openai_client):
    chat_completion = openai_client.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": "Tell me about dspy library"}]
    )
    chat_completion
    return


@app.cell
def _(MODEL, openai_client):
    # Test tool use with function calling
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    tool_completion = openai_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "What's the weather like in Tokyo? Use celsius."}],
        tools=tools,
        tool_choice="auto",
    )

    tool_completion
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Setup""")
    return


@app.cell
def _():
    import marimo as mo
    from dotenv import load_dotenv
    from openai import OpenAI

    assert load_dotenv(), "Failed to load .env file"
    return OpenAI, mo


@app.cell
def _(OpenAI):
    MODEL = "Qwen/Qwen2.5-3B-Instruct"

    openai_client = OpenAI()
    return MODEL, openai_client


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
