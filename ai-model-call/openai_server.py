import os
from typing import Dict, Any
import openai
from fastmcp import FastMCP

# Initialize API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Create OpenAI MCP server
server = FastMCP("Call OpenAI o1 model")


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
    # Initialize API client
    openai_client = None
    if OPENAI_API_KEY:
        openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

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