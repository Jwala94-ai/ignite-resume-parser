"""LLM client for AI processing"""
from openai import OpenAI

class LLMClient:

    def __init__(self, api_key):

        self.client = OpenAI(
            api_key=api_key
        )

    def parse_resume(self, prompt):

        response = self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.choices[0].message.content