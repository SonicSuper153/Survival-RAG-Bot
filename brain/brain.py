import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class Brain:
    def __init__(self):
        self.OLLAMA_API_BASE = os.getenv("OLLAMA_API_BASE")

    def getLLM(self) -> OpenAI:
        return OpenAI(
            base_url=self.OLLAMA_API_BASE,
            api_key="ollama"  
        )

    def getEmbeddings(self, text: str):
        client = self.getLLM()
        response = client.embeddings.create(
            model="nomic-embed-text:v1.5", 
            input=text
        )
        return response.data[0].embedding
    
    
