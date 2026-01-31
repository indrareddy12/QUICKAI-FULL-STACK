from typing import Dict, Any
import google.generativeai as genai
from .base_agent import BaseAgent
from core.config import settings

class CommunicationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Communication Agent")
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Drafts a legal document.
        Expected input: {"doc_type": str, "case_facts": str}
        """
        doc_type = input_data.get("doc_type")
        facts = input_data.get("case_facts")
        
        if not self.model:
            return {"status": "mock", "data": f"[DRAFT {doc_type}]\n\nBased on: {facts}..."}

        prompt = f"Draft a formal Indian legal document of type '{doc_type}' based on these facts:\n{facts}"
        
        try:
            response = self.model.generate_content(prompt)
            return {
                "status": "success",
                "data": response.text
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
