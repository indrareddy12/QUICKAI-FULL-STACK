from core.config import settings
import google.generativeai as genai
from models.schemas import LegalDossier, LawyerMatch
from core.prompts import LEGAL_SYSTEM_PROMPT, CASE_ANALYSIS_TEMPLATE, LAWYER_MATCHING_PROMPT
import json

class AnalysisEngine:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=LEGAL_SYSTEM_PROMPT)
        else:
            self.model = None
            print("WARNING: GEMINI_API_KEY not set. Using Mock Mode.")

    def analyze_case(self, description: str, doc_texts: str = "") -> LegalDossier:
        """
        Analyzes case description + extracted text from documents.
        """
        full_context = f"{description}\n\nRELEVANT DOCUMENTS:\n{doc_texts}"
        
        if not self.model:
            return self._mock_dossier(description)
        
        prompt = CASE_ANALYSIS_TEMPLATE.format(case_description=full_context)
        
        try:
            # Force JSON response for structured data
            response = self.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            data = json.loads(response.text)
            return LegalDossier(**data)
        except Exception as e:
            print(f"AI Error: {e}")
            return self._mock_dossier(description)

    def match_lawyers(self, category: str, location: str):
        # In a real app, this would query a lawyer database.
        # Here we use logic to map category -> lawyer types.
        return [
            LawyerMatch(
                name="Adv. Sharma & Associates",
                specialization=category,
                contact="+91-9876543210",
                location=location
            ),
             LawyerMatch(
                name="Legal Aid Clinic",
                specialization="General",
                contact="+91-1122334455",
                location=location
            )
        ]

    def _mock_dossier(self, description: str) -> LegalDossier:
        return LegalDossier(
            case_summary=f"(MOCK) Analysis of: {description[:50]}...",
            potential_charges=["IPC 420 (Cheating)", "IPC 406 (Criminal Breach of Trust)"],
            recommended_actions=["File an FIR", "Preserve Evidence", "Consult Criminal Lawyer"]
        )
