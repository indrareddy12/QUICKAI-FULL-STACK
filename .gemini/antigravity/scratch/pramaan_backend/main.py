from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from core.database import engine, Base, get_db
from models import models, schemas
from core.ai_service import AnalysisEngine
from services.ingestion_service import IngestionService
from services.generator_service import GeneratorService

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pramaan AI Backend", version="2.0 (Scalable)")
ai_service = AnalysisEngine()

@app.get("/")
def home():
    return {"message": "Pramaan AI Legal Aid Backend (Production Ready) is Running"}

# --- INGESTION LAYER ---
@app.post("/ingest/document", response_model=schemas.DocumentResponse)
async def upload_document(
    case_id: int, 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    """Uploads a PDF/Text document and associates it with a case."""
    return await IngestionService.process_document(db, file, case_id)

@app.post("/ingest/voice", response_model=schemas.DocumentResponse)
async def upload_voice_note(
    case_id: int, 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    """Uploads an audio file and transcribes it."""
    return await IngestionService.process_voice(db, file, case_id)

# --- ANALYSIS LAYER ---
@app.post("/case/create", response_model=int)
def create_case(db: Session = Depends(get_db)):
    """Creates a new empty case session."""
    case = models.CaseLog()
    db.add(case)
    db.commit()
    db.refresh(case)
    return case.id

@app.post("/analyze", response_model=schemas.LegalDossier)
async def analyze_case(
    case_input: schemas.CaseInput, 
    case_id: int, 
    db: Session = Depends(get_db)
):
    """
    Analyzes case description + previously uploaded documents for that case.
    """
    # 1. Fetch relevant document texts
    docs = db.query(models.Document).filter(models.Document.case_id == case_id).all()
    combined_doc_text = "\n".join([f"Document {d.filename}: {d.extracted_text}" for d in docs])
    
    # 2. Run AI Analysis
    dossier = ai_service.analyze_case(case_input.description, combined_doc_text)
    
    # 3. Save User Input & Result to DB
    case = db.query(models.CaseLog).filter(models.CaseLog.id == case_id).first()
    if case:
        case.user_description = case_input.description
        case.analysis_json = dossier.dict()
        db.commit()
    
    dossier.case_id = case_id
    return dossier

@app.post("/find-lawyer", response_model=List[schemas.LawyerMatch])
async def find_lawyer(request: schemas.LawyerRequest):
    return ai_service.match_lawyers(request.category, request.location)

# --- GENERATION LAYER ---
@app.post("/generate-doc", response_model=schemas.GeneratedDocResponse)
async def generate_legal_doc(
    request: schemas.DocGenerationRequest,
    db: Session = Depends(get_db)
):
    """Generates a legal document (e.g., Notice) based on case facts."""
    try:
        doc = GeneratorService.generate_document(
            db, 
            request.case_id, 
            request.doc_type, 
            request.extra_details
        )
        return doc
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Clean up uploads on restart in dev
    import os
    import shutil
    if os.path.exists("uploads"):
        shutil.rmtree("uploads")
    os.makedirs("uploads")
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
