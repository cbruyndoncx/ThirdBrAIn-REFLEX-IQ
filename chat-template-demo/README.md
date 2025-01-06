# Chat with Reflex Docs

This is a demo app made using the [Chat template](https://github.com/reflex-dev/reflex-chat) from [Reflex](https://github.com/reflex-dev/reflex), [Llama Index](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/), [Traceloop](https://www.traceloop.com/docs/openllmetry/getting-started-python) and OpenAI.

## Prerequisites

- OpenAI API key: the app uses OpenAI embedding and chat functionality.
- Traceloop API key: the app traces the function call to OpenAI and export to Traceloop dashboard.

## Requirements

```bash
reflex>=0.4.7
llama-index
traceloop-sdk
```

## Steps to Run

### Environment Variables

```bash
export TRACELOOP_API_KEY=12345yourkey
export OPENAI_API_KEY=sk-your-key
```

### Run the Reflex App

This app is based on [Reflex](https://github.com/reflex-dev/reflex) framework. In the top level directory (this directory has a file named `rxconfig.py`), run the following commands to run the app:

```bash
reflex init
reflex run
```

Then go to `https://localhost:3000` or another URL shown in the terminal when the app is running. Chat and get the results based on the reflex documentation.

### Monitor Your App on Traceloop

Go to the traceloop dashboard, you can see stats such as the tokens and models used for OpenAI calls.
