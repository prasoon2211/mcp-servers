import os
import json
from typing import Dict, Any, List
from fastmcp import FastMCP
from google import genai
import openai

# Initialize API keys from environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize API clients
if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Keep using OpenAI client initialization for openai >= 1.0
if OPENAI_API_KEY:
    openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Create MCP server
server = FastMCP("Call Gemini 2.5 Pro and OpenAI o1 models")

@server.tool()
def ask_gemini_2_5_pro(
    prompt: str,
) -> Dict[str, Any]:
    """Call Gemini 2.5 Pro to solve problems requiring lots of context.

    Args:
        prompt: The user prompt including all the relevant context to solve the problem.
    Returns:
        The model's response
    """
    if not gemini_client:
        return {"error": "Gemini client not initialized. Check GEMINI_API_KEY."}

    try:
        # Generate content using the client's models interface
        response = gemini_client.models.generate_content(
            model="gemini-2.5-pro-preview-03-25",
            contents=[prompt],
        )

        return {"content": response.text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}


@server.tool()
def ask_openai_o1(
    prompt: str,
) -> Dict[str, Any]:
    """Call OpenAI's o1 model to solve problems requiring difficult reasoning.

    Args:
        prompt: The user prompt to send to the model including all the relevant context to solve the problem.
    Returns:
        The model's response
    """
    if not openai_client:
        return {"error": "OpenAI client not initialized. Check OPENAI_API_KEY."}

    try:
        response = openai_client.responses.create(
            model="o1",
            input=prompt
        )

        return {"content": response.output_text}
    except Exception as e:
        return {"error": f"OpenAI API call failed: {str(e)}"}

if __name__ == "__main__":
    server.run()
