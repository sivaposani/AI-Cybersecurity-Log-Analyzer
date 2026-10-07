import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_alert(alert):
    prompt = f"""
You are a cybersecurity analyst.

Analyze this security alert:

{alert}

Explain:
1. What the alert means
2. Why it is suspicious
3. What action should be taken

Keep the explanation concise and practical.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text