# AI Model Call MCP Server

An MCP server for Claude Code that provides tool calls to various AI models:

- Gemini 2.5 Pro
- OpenAI o1

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Set up API keys:

```bash
export GEMINI_API_KEY=your_gemini_api_key
export OPENAI_API_KEY=your_openai_api_key
```

3. Test the server (gemini example):

```bash
source .venv/bin/activate
fastmcp run gemini_server.py
```

4. Configure Claude Code:

```bash
claude mcp add-json ask_openai '{ "command": "uv", "args": [ "--directory", "<FULL PATH TO THE ROOT DIR>", "run", "openai_server.py" ] }'

OR

claude mcp add-json ask_gemini '{ "command": "uv", "args": [ "--directory", "<FULL PATH TO THE ROOT DIR>", "run", "gemini_server.py" ] }'
```

## Tool Usage

Just ask claude code to use `ask_openai` or `ask_gemini` to do things and it will work
