# AI Model Call MCP Server

An MCP server for Claude Code that provides tool calls to various AI models:
- Gemini 2.5 Pro
- OpenAI o1

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Set up API keys:
```bash
export GEMINI_API_KEY=your_gemini_api_key
export OPENAI_API_KEY=your_openai_api_key
```

3. Run the server:
```bash
python main.py
```

4. Configure Claude Code:
```bash
claude mcp add ai-model-call "python /path/to/main.py"
```

## Tool Usage

### ask_gemini_2_5_pro
Call Gemini 2.5 Pro with a prompt:
```
{
  "prompt": "Explain quantum computing in simple terms",
  "system_prompt": "You are a helpful AI assistant specialized in science education.",
  "temperature": 0.7,
  "max_tokens": 1024
}
```

### ask_openai_o1
Call OpenAI's o1 model with a prompt:
```
{
  "prompt": "Solve this math problem step by step: x^2 + 5x + 6 = 0",
  "system_prompt": "You are a math tutor. Show your work clearly.",
  "temperature": 0.2,
  "max_tokens": 512
}
```