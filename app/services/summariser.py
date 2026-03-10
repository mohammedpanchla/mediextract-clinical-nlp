import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SUMMARY_PROMPT = """You are a senior clinical documentation specialist.
Based on the structured patient data below, write a concise clinical summary.

Rules:
- 3 to 5 sentences maximum
- Written in professional clinical language
- Cover: who the patient is, why admitted, what was done, key medications, follow-up plan
- Do NOT invent any information not present in the data
- If a field is null or missing, skip it — do not mention it
- Return plain text only, no bullet points, no headers, no markdown

Structured patient data:
{data}
"""

def generate_summary(extracted_data: dict) -> dict:
    import json
    prompt = SUMMARY_PROMPT.format(data=json.dumps(extracted_data, indent=2))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a clinical documentation specialist. Write concise, accurate clinical summaries."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    summary = response.choices[0].message.content.strip()
    return {"success": True, "summary": summary}