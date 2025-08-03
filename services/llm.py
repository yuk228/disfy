from typing import cast

from litellm import completion

from config.settings import GEMINI_API_KEY


async def generate_text_with_gemini(
    prompt: str, max_tokens: int = 1024, image_url: str = None
) -> str:
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            {"role": "user", "content": prompt},
        ]
        + ([{"role": "user", "content": image_url}] if image_url else []),
        max_tokens=max_tokens,
        api_key=GEMINI_API_KEY,
    )
    return cast(str, response.choices[0].message.content)
