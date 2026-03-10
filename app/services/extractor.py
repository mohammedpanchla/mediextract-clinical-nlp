import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

EXTRACTION_PROMPT = """You are a clinical data extraction assistant.
Extract the following fields from the clinical note below.
Return ONLY valid JSON, nothing else. No explanation, no markdown, just raw JSON.

Fields to extract:
- patient_age (number or null)
- patient_gender (string or null)
- admission_reason (string or null)
- conditions (list of strings)
- medications (list of strings with dosage if mentioned)
- blood_pressure (string or null)
- key_vitals (object with any vitals mentioned)
- hospital_stay_days (number or null)
- discharge_plan (string or null)
- follow_up (string or null)
- document_type (what type of document this is)

CRITICAL MEDICATION EXTRACTION RULE:
If discharge medications are present, extract ONLY discharge medications.

Discharge medications are typically under sections like:
"Medications on discharge"
"Discharge medications"
"Medications at discharge"

DO NOT include medications listed under:
"Medication history"
"Home medications"
"Medications on admission"

If discharge medications exist, ignore admission medications completely.

If a field is not mentioned, return null for that field.
For lists, return empty list [] if nothing found.

Clinical note:
{text}
"""

def extract_from_note(clinical_text: str) -> dict:
    prompt = EXTRACTION_PROMPT.format(text=clinical_text)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a medical data extraction assistant. Always return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    raw = response.choices[0].message.content.strip()

    # Clean up if model wrapped in markdown
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    try:
        return {"success": True, "data": json.loads(raw)}
    except json.JSONDecodeError:
        return {"success": False, "error": "Model returned invalid JSON", "raw": raw}





