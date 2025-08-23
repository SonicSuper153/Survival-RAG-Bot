import os
from brain import Brain
from config import SURVIVAL_BOT

class Survival:
    def __init__(self):
        self.brain = Brain()

    def output(self) -> str:
        client = self.brain.getLLM()
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": SURVIVAL_BOT}
            ]
        )

        # Extract response text
        if hasattr(response, "choices") and response.choices:
            return response.choices[0].message.content.strip()
        return "No response generated."