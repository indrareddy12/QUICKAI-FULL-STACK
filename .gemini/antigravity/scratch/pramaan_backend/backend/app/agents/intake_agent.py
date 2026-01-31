from typing import Dict, Any
from .base_agent import BaseAgent

class IntakeAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intake Agent")

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates the initial case input.
        Expected input: {"description": str, "case_id": int}
        """
        description = input_data.get("description")
        case_id = input_data.get("case_id")

        if not description or not isinstance(description, str):
            raise ValueError("Invalid case description")
        
        if not case_id:
             raise ValueError("Case ID is required")

        return {
            "status": "success",
            "data": {
                "case_id": case_id,
                "description": description,
                "validated": True
            }
        }
