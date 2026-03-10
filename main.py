from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.services.extractor import extract_from_note
from app.services.formatter import format_output
import os

app = FastAPI(title="MediExtract", version="1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

class NoteRequest(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html") as f:
        return f.read()

@app.get("/health")
async def health():
    return {"status": "ok", "model": "llama-3.3-70b-versatile"}

@app.post("/extract")
async def extract(request: NoteRequest):
    if not request.text.strip():
        return {"success": False, "error": "No text provided"}
    result = extract_from_note(request.text)
    final = format_output(result)
    return final


from app.services.summariser import generate_summary

class SummaryRequest(BaseModel):
    data: dict

@app.post("/summarise")
async def summarise(request: SummaryRequest):
    if not request.data:
        return {"success": False, "error": "No data provided"}
    result = generate_summary(request.data)
    return result