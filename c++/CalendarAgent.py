# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import time

from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3.5-flash"
    
    # Prompt updated to get a direct confirmation message instead of questions
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Write a final confirmation message for a meeting scheduled for tomorrow morning at 10:00 AM IST called 'Project Sync' for 1 hour. Do not ask me any follow-up questions."""),
            ],
        ),
    ]
    
    tools = []
    
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="MEDIUM",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")
        
        time.sleep(4)

if __name__ == "__main__":
    generate()-