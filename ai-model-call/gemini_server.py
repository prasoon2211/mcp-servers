import os
from typing import Dict, Any
from google import genai
from fastmcp import FastMCP

# Initialize API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create Gemini MCP server
server = FastMCP("Call Gemini 2.5 Pro model")

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
    # Initialize API client
    gemini_client = None
    if GEMINI_API_KEY:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)

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


if __name__ == "__main__":
    server.run()