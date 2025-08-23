import os
from brain import Brain
from config import SUMMARIZE_TEMPLATE  # Externalized template

class Agent:
    def __init__(self):
        self.brain = Brain()

    def output(self, query: str, context: str) -> str:
        prompt = SUMMARIZE_TEMPLATE.format(
            query=query,
            context=context
        )
        client = self.brain.getLLM()
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract response text
        if hasattr(response, "choices") and response.choices:
            return response.choices[0].message.content.strip()
        return "No response generated."
