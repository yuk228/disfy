import os
from typing import cast
from litellm import completion

async def generate_text_with_gemini(prompt: str, max_tokens: int = 1024) -> str:
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        api_key=os.getenv("GEMINI_API_KEY"),
    )
    return cast(str, response.choices[0].message.content)