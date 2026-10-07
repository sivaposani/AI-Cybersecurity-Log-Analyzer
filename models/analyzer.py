import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_alert(alert):
    prompt = f"""
You are a cybersecurity analyst.

Analyze this security alert:

{alert}

Return your answer as JSON with exactly these fields:

- threat_summary: a short explanation of the threat
- risk_level: LOW, MEDIUM, HIGH, or CRITICAL
- recommended_actions: a list of practical actions
- confidence: a number between 0 and 1
"""

    try:
        response = client.responses.create(
            model="gpt-6-luna",
            input=prompt
        )

        return json.loads(response.output_text)

    except Exception as error:
        print("AI analysis failed. Using fallback analysis.")

        return {
            "threat_summary": "AI analysis was unavailable.",
            "risk_level": alert["severity"],
            "recommended_actions": [
                "Review the security alert manually.",
                "Check authentication logs.",
                "Investigate the source IP."
            ],
            "confidence": 0.0
        }