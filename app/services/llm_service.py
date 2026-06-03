from groq import Groq
from dotenv import load_dotenv
import os

# load_dotenv(dotenv_path=r"C:\Users\mahesh yadav\OneDrive\Desktop\fanincial_chatbot\ai_financial_chatbot\.env")
load_dotenv()
print("DEBUG KEY:", os.getenv("GROQ_API_KEY"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_llm(question, context):

    prompt = f"""
You are a Personal Financial Assistant specialized in Mutual Funds.

Your role is to help users understand mutual funds using:
1. Information from the provided document context, and 
2. Reliable general knowledge about mutual funds if context is missing.

Primary Rules:
1. If answer exists in the provided context, use it as primary source.
2. If not, use general financial knowledge.
3. Do NOT generate misleading or harmful financial advice.
4. If unsure, ask user to verify from trusted sources.

Safety Rules:
- Avoid risky financial advice.
- Do not recommend specific investments unless clearly mentioned.
- Avoid speculation.

Response Guidelines:
- Keep answers clear, concise, beginner-friendly.
- Focus only on relevant info.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content