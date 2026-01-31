from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

# --- SHARED ---
class DocumentBase(BaseModel):
    filename: str
    file_type: str

class DocumentCreate(DocumentBase):
    file_path: str
    extracted_text: Optional[str] = None

class DocumentResponse(DocumentBase):
    id: int
    upload_time: datetime

    class Config:
        from_attributes = True

# --- INPUTS ---
class CaseInput(BaseModel):
    description: str
    related_document_ids: Optional[List[int]] = []

class LawyerRequest(BaseModel):
    category: str
    location: str

class DocGenerationRequest(BaseModel):
    case_id: int
    doc_type: str  # "notice", "affidavit", "plaint"
    extra_details: Optional[dict] = {}

# --- OUTPUTS ---
class LegalDossier(BaseModel):
    case_summary: str
    potential_charges: List[str]
    recommended_actions: List[str]
    case_id: Optional[int] = None

class LawyerMatch(BaseModel):
    name: str
    specialization: str
    contact: str
    location: str

class GeneratedDocResponse(BaseModel):
    id: int
    doc_type: str
    content: str
    created_at: datetime
    
    class Config:
        from_attributes = True
