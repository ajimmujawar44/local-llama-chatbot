from openai import OpenAI

from config import (
    API_KEY,
    BASE_URL,
    MODEL,
)


class LlamaClient:
    """
    Client for communicating with LLaMA
    through Docker Model Runner.
    """

    def __init__(self):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY,
        )

    def chat(
        self,
        messages,
        temperature=0.7,
        max_tokens=512,
    ):
        """
        Generate a complete response.
        """

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content

    def stream_chat(
        self,
        messages,
        temperature=0.7,
        max_tokens=512,
    ):
        """
        Generate a streaming response.
        """

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )

        for chunk in response:

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                yield content