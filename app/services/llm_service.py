import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class LLMService:
    def generate_sql(self, query: str, context: str) -> str:
        prompt = f"""
You are a SQL expert. Given the database schema below, 
write a safe SELECT SQL query for the question:

Schema:
{context}

User Question:
{query}

Only write the SQL query — do not explain it.
        """
        
        

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content


