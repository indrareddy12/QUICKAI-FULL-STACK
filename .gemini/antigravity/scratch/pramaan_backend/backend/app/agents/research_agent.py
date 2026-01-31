from typing import Dict, Any
import google.generativeai as genai
from .base_agent import BaseAgent
from core.config import settings

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Identifies relevant laws and precedents using web search.
        Expected input: {"case_description": str}
        """
        description = input_data.get("case_description")
        
        # 1. Web Search for latest laws/precedents
        search_results = ""
        try:
            from duckduckgo_search import DDGS
            with DDGS() as ddgs:
                # Search for Indian laws related to the case
                query = f"Indian law sections and precedents for: {description[:100]}"
                results = list(ddgs.text(query, max_results=5))
                search_results = "\n".join([f"- {r['title']}: {r['body']} ({r['href']})" for r in results])
        except Exception as e:
            print(f"Search Error: {e}")
            search_results = "Search failed, relying on internal knowledge."

        if not self.model:
            return {"status": "mock", "data": f"IPC 420 (Mock)\nSearch Results:\n{search_results}"}

        # 2. Synthesize with LLM
        prompt = f"""
        Identify relevant Indian laws, acts, and sections for the following case description.
        
        CASE:
        {description}
        
        WEB RESEARCH RESULTS:
        {search_results}
        
        Provide a concise legal summary citing relevant sections and 1-2 precedents if found.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return {
                "status": "success",
                "data": response.text
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
