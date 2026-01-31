from typing import Dict, Any
from .base_agent import BaseAgent
from models.schemas import LawyerMatch

class LawyerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Lawyer Agent")

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Matches lawyers.
        Expected input: {"category": str, "location": str}
        """
        category = input_data.get("category", "General")
        location = input_data.get("location", "India")
        
        # Mock logic
        matches = [
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
        
        return {
            "status": "success",
            "data": [m.dict() for m in matches]
        }
