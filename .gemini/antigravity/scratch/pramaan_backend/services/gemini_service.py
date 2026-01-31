import google.generativeai as genai
import json
import logging
from typing import Any, Dict, List, Union
from core.config import settings

logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
            logger.warning("GEMINI_API_KEY not set. Service will return mock data.")

    async def generate_structured(self, prompt: str, schema: Any) -> Union[Dict[str, Any], List[Any]]:
        """
        Generates structured data (JSON) from the LLM.
        """
        if not self.model:
            # Mock Response for structured calls when key is missing
            return {
                "sections": [{"section": "MOCK-420", "code": "IPC", "title": "Cheating (Mock)", "description": "Mock description due to missing API Key", "punishment": "3 Years", "relevance": "High"}],
                "score": 45,
                "strengths": ["Mock Strength 1"],
                "weaknesses": ["Mock Weakness 1"],
                "evidence": [{"type": "Mock Doc", "description": "Upload documents", "importance": "High", "priority": "critical"}],
                "actions": ["Configure API Key", "Consult Lawyer"]
            }

        # Explicitly ask for JSON in the prompt
        enhanced_prompt = f"{prompt}\n\nPlease respond in valid JSON format matching this schema:\n{json.dumps(schema, indent=2)}"
        
        try:
            response = self.model.generate_content(
                enhanced_prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            return json.loads(response.text)
        except Exception as e:
            logger.error(f"Gemini Generation Error: {e}")
            raise e
