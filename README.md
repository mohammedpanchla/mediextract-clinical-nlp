# MediExtract — Clinical Intelligence Platform

> Transform unstructured clinical notes into structured medical intelligence using Large Language Models.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-yellow)](https://muhammedpanchla-mediextract-clinical-nlp.hf.space)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com)
[![Model](https://img.shields.io/badge/Model-Llama%203.3%2070B-purple)](https://groq.com)

---

## What is MediExtract?

MediExtract is a clinical NLP tool that takes unstructured medical documents — discharge summaries, referral letters, clinical notes — and extracts all key structured fields in seconds. It also auto-generates a concise clinical narrative summary using a fine-tuned LLM prompt.

Built to demonstrate the application of large language models in real-world clinical workflows, MediExtract bridges the gap between raw clinical prose and structured, actionable data.

---

## Features

- **Structured Extraction** — Automatically extracts patient age, gender, admission reason, diagnoses, medications, blood pressure, key vitals, hospital stay, discharge plan, and follow-up
- **AI Clinical Summary** — Generates a professional 3–5 sentence clinical narrative from extracted data
- **Collapsible Summary Card** — Toggle the summary open/closed for a cleaner view
- **Copy Buttons** — One-click copy for summary, individual fields, and full JSON
- **Export JSON** — Download structured data as a `.json` file
- **Export CSV** — Download structured data as a `.csv` file for research use
- **Discharge Medication Priority** — Automatically prioritises discharge medications over admission medications
- **Clear All** — Reset input and output in one click
- **Professional UI** — Clean, hospital-grade interface built with vanilla HTML/CSS/JS

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python) |
| LLM | Llama 3.3 70B via Groq API |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker + Hugging Face Spaces |
| Fonts | DM Serif Display, DM Mono, Instrument Sans |

---

## Extracted Fields

| Field | Description |
|-------|-------------|
| `patient_age` | Age in years |
| `patient_gender` | Male / Female / Other |
| `admission_reason` | Primary reason for admission |
| `conditions` | List of diagnoses and conditions |
| `medications` | Discharge medications with dosage |
| `blood_pressure` | BP reading from document |
| `key_vitals` | Heart rate, SpO2, temperature, etc. |
| `hospital_stay_days` | Length of inpatient stay |
| `discharge_plan` | Discharge instructions and plan |
| `follow_up` | Follow-up appointments and referrals |
| `document_type` | Auto-detected document type |

---

## Live Demo

🔗 [https://muhammedpanchla-mediextract-clinical-nlp.hf.space](https://muhammedpanchla-mediextract-clinical-nlp.hf.space)

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/muhammedpanchla/mediextract-clinical-nlp.git
cd mediextract-clinical-nlp
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the server

```bash
uvicorn main:app --reload
```

### 6. Open in browser

```
http://127.0.0.1:8000
```

---

## Project Structure

```
mediextract-clinical-nlp/
├── app/
│   ├── __init__.py
│   └── services/
│       ├── __init__.py
│       ├── extractor.py       # Groq API + prompt engineering
│       ├── formatter.py       # JSON validation and formatting
│       └── summariser.py      # Clinical narrative generation
├── static/
│   └── index.html             # Frontend interface
├── main.py                    # FastAPI routes
├── requirements.txt
├── Dockerfile
└── .env                       # Not committed — add your own
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the frontend |
| `GET` | `/health` | Health check |
| `POST` | `/extract` | Extract structured fields from clinical note |
| `POST` | `/summarise` | Generate clinical narrative from extracted data |

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/extract" \
  -H "Content-Type: application/json" \
  -d '{"text": "Patient is a 67 year old male admitted with chest pain..."}'
```

### Example Response

```json
{
  "success": true,
  "data": {
    "patient_age": 67,
    "patient_gender": "male",
    "admission_reason": "chest pain",
    "conditions": ["hypertension", "type 2 diabetes"],
    "medications": ["aspirin 75mg once daily", "clopidogrel 75mg once daily"],
    "blood_pressure": "160/90",
    "key_vitals": {"heart_rate": "88 bpm"},
    "hospital_stay_days": 3,
    "discharge_plan": "stable condition",
    "follow_up": "cardiology review in 2 weeks",
    "document_type": "discharge summary"
  }
}
```

---

## Part of the Clinical AI Suite

MediExtract is part of a broader healthcare AI portfolio:

| Project | Description | Link |
|---------|-------------|------|
| **ClinAI** | Multi-model clinical diagnostics platform (brain tumor, ECG, heart disease, stroke) | [Live](https://muhammedpanchla-clinai-flagship.hf.space) |
| **MediExtract** | Clinical NLP — structured extraction from unstructured notes | [Live](https://muhammedpanchla-mediextract-clinical-nlp.hf.space) |

---

## Disclaimer

> MediExtract is built for research and educational purposes only. It is not a certified medical device and should not be used for clinical decision-making.

---

## Author

**Mohammed Panchla**
- GitHub: [@muhammedpanchla](https://github.com/muhammedpanchla)
- LinkedIn: [muhammedpanchla](https://linkedin.com/in/muhammedpanchla)
