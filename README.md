# MediExtract — Clinical Intelligence Platform

> Transform unstructured clinical notes into structured medical intelligence using Large Language Models.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-yellow)](https://muhammedpanchla-mediextract-clinical-nlp.hf.space)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com)
[![Model](https://img.shields.io/badge/Model-Llama%203.3%2070B-purple)](https://groq.com)

---

# 🏥 MediExtract — Clinical Intelligence Platform
### LLM-Powered Structured Extraction from Unstructured Clinical Notes (FastAPI + Llama 3.3 70B)

---

## 📌 Project Overview

Every day, thousands of clinical documents — discharge summaries, referral letters, and clinical notes — are written in unstructured prose. Extracting key medical information from this text manually is time-consuming and error-prone.

This project builds an AI-powered clinical NLP tool that takes any unstructured medical document and automatically extracts all key structured fields in seconds — plus generates a concise clinical narrative summary.

```
Input:  Unstructured clinical note / discharge summary / referral letter
Output: Structured JSON with 11 medical fields + AI clinical summary
```

The system uses:

• **Llama 3.3 70B** via Groq API — for fast, accurate field extraction  
• **FastAPI** — production-grade Python backend  
• **Prompt Engineering** — carefully crafted clinical extraction prompts  
• **Clinical Summarisation** — auto-generated 3–5 sentence narrative  

#### 🧠 LIVE DEMO :- https://muhammedpanchla-mediextract-clinical-nlp.hf.space

---

## 🎯 Project Objective

The primary goal is to convert raw clinical prose into structured, machine-readable data.

Extracted fields:

| Field | Description |
|---|---|
| `patient_age` | Age in years |
| `patient_gender` | Male / Female / Other |
| `admission_reason` | Primary reason for admission |
| `conditions` | List of diagnoses and conditions |
| `medications` | Discharge medications with dosage |
| `blood_pressure` | BP reading from document |
| `key_vitals` | Heart rate, SpO2, temperature, etc. |
| `hospital_stay_days` | Length of inpatient stay |
| `discharge_plan` | Discharge instructions |
| `follow_up` | Follow-up appointments and referrals |
| `document_type` | Auto-detected document type |

---

## 🔬 NLP Pipeline for Clinical Documents

This project applies large language models to unstructured medical text.

| Aspect | Value |
|---|---|
| Data type | Unstructured clinical text |
| Task | Named entity extraction + summarisation |
| Input | Any clinical document (free text) |
| Output | Structured JSON + clinical narrative |
| Domain | Healthcare AI / Clinical NLP |

---

## 🧠 Architecture Overview

Two LLM calls are made per document — extraction then summarisation.

---

### Step 1: Structured Field Extraction

Prompt-engineered LLM call that extracts all 11 clinical fields.

Extraction flow:

```
Raw Clinical Document (free text)
↓
Extraction Prompt (prompt engineering)
↓
Llama 3.3 70B via Groq API (temperature=0.1)
↓
Raw JSON Response
↓
JSON Validation + Formatting
↓
Structured Clinical Data (11 fields)
```

Purpose: Convert unstructured prose into machine-readable structured data.

---

### Step 2: Clinical Narrative Summary

Second LLM call that takes the extracted JSON and generates a clinical summary.

Summary flow:

```
Structured JSON (from Step 1)
↓
Summarisation Prompt (clinical language)
↓
Llama 3.3 70B via Groq API (temperature=0.3)
↓
3–5 Sentence Clinical Narrative
```

Purpose: Generate a human-readable summary in professional clinical language.

---

## ✨ Features

• **Structured Extraction** — 11 clinical fields extracted from any document  
• **AI Clinical Summary** — auto-generated professional clinical narrative  
• **Collapsible Summary Card** — toggle open/close like an FAQ accordion  
• **Copy Buttons** — one-click copy for summary, individual fields, and full JSON  
• **Export JSON** — download structured data as `.json`  
• **Export CSV** — download structured data as `.csv` for research  
• **Discharge Medication Priority** — discharge meds prioritised over admission meds  
• **Clear All** — reset input and output in one click  
• **Professional UI** — clean, hospital-grade interface  

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python) |
| LLM | Llama 3.3 70B via Groq API |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker + Hugging Face Spaces |
| Fonts | DM Serif Display, DM Mono, Instrument Sans |

---

## 🔧 Training Configuration

| Parameter | Value |
|---|---|
| Model | Llama 3.3 70B Versatile |
| API | Groq (free tier) |
| Extraction Temperature | 0.1 (low — consistent outputs) |
| Summary Temperature | 0.3 (slightly creative) |
| Max Tokens | 1000 (extraction) / 300 (summary) |
| Framework | FastAPI + Python |

---

## 📈 Evaluation

The following criteria were used to evaluate extraction quality:

| Metric | Result |
|---|---|
| Field extraction accuracy | High — tested on diverse clinical documents |
| Medication priority (discharge over admission) | Correctly handled |
| Null field handling | Returns null for missing fields |
| Document type detection | Auto-detected from content |
| Summary quality | Professional clinical language |

---

## 🚀 Full Pipeline

Complete workflow:

```
Clinical Document Input
↓
Text Validation
↓
Extraction Prompt Construction
↓
Groq API Call (Llama 3.3 70B)
↓
JSON Parsing + Validation
↓
Structured Fields (11 fields)
↓
Summarisation Prompt Construction
↓
Groq API Call (Llama 3.3 70B)
↓
Clinical Narrative (3–5 sentences)
↓
Frontend Render (fields + summary + export)
```

---

## 🌐 Web Application

A complete FastAPI deployment provides a clinical-grade interface.

#### LINK: https://muhammedpanchla-mediextract-clinical-nlp.hf.space

**Features:**
- Paste any clinical document into the text area
- Click Analyse Document — extraction + summary in ~3 seconds
- Collapsible AI Clinical Summary card at the top
- All 11 structured fields displayed with status indicators
- Copy buttons on summary, individual fields, and full JSON
- Export to JSON or CSV with one click
- Load Sample Discharge Summary for quick demo
- Clear All to reset everything instantly

---

## 📁 Repository Structure

```
mediextract-clinical-nlp/
│
├── app/
│   ├── __init__.py
│   └── services/
│       ├── __init__.py
│       ├── extractor.py        ← Groq API + extraction prompt
│       ├── formatter.py        ← JSON validation and formatting
│       └── summariser.py       ← Clinical narrative generation
│
├── static/
│   └── index.html              ← Frontend interface
│
├── main.py                     ← FastAPI routes
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
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
    "discharge_plan": "stable condition, avoid driving 4 weeks",
    "follow_up": "cardiology review in 2 weeks",
    "document_type": "discharge summary"
  }
}
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/muhammedpanchla/mediextract-clinical-nlp.git
cd mediextract-clinical-nlp
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free key at [console.groq.com](https://console.groq.com)

### 5. Run the server

```bash
uvicorn main:app --reload
```

### 6. Open in browser

```
http://127.0.0.1:8000
```

---

## ⚙️ Technologies Used

**LLM & API**  
• Groq API  
• Llama 3.3 70B Versatile  

**Backend**  
• FastAPI  
• Uvicorn  
• Python-dotenv  

**Frontend**  
• HTML5  
• CSS3  
• JavaScript (Vanilla)  

**Deployment**  
• Docker  
• Hugging Face Spaces  

---

## 🔬 Technical Highlights

• End-to-end clinical NLP pipeline  
• LLM prompt engineering for structured medical extraction  
• Two-stage pipeline — extraction then summarisation  
• Discharge medication priority over admission medications  
• JSON validation and null field handling  
• Production FastAPI backend with Docker deployment  
• Clinical-grade UI with copy, export, and collapse features  

---

## 🏥 Clinical and Business Impact

| Stakeholder | Benefit |
|---|---|
| Doctors | Instant structured summary from any clinical note |
| Hospitals | Automate data entry from discharge summaries |
| Researchers | Export structured patient data to CSV for analysis |
| Engineers | REST API for integration into EHR systems |
| Healthcare AI | Scalable clinical NLP pipeline |

---

## 🎯 Future Improvements

• Multi-patient batch processing — upload folder of notes, get one CSV  
• PDF upload support — extract directly from scanned documents  
• FHIR-compatible output — standard healthcare data format  
• Fine-tuned clinical model — trained specifically on medical NLP  
• Confidence scores per field  

---

## 🤝 Part of the Clinical AI Suite

MediExtract is part of a broader healthcare AI portfolio:

| Project | Description | Link |
|---|---|---|
| **ClinAI** | Multi-model diagnostics — brain tumor, ECG, heart disease, stroke | [Live Demo](https://muhammedpanchla-clinai-flagship.hf.space) |
| **MediExtract** | Clinical NLP — structured extraction from unstructured notes | [Live Demo](https://muhammedpanchla-mediextract-clinical-nlp.hf.space) |

---

## ⚠️ Disclaimer

MediExtract is built for research and educational purposes only. It is not a certified medical device and should not be used for clinical decision-making.

---

## 👨‍💻 Author

**Mohammed Panchla**

Machine Learning Engineer focused on Healthcare AI and Clinical NLP Systems.

---

## ⭐ If you found this project useful, consider giving it a star!
