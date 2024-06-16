from fastapi import APIRouter, HTTPException
from models.suggestModel import TaskRequest, TechnicianSuitability
from controllers import suggestController
from typing import List, Dict

router = APIRouter()

@router.post("/technician-to-task", response_model=List[TechnicianSuitability])
async def suggest_technician_to_task(task_request: TaskRequest):
    # This is a mock response. In a real application, you would have logic here to determine the suitability.

    try:
        suggestions = suggestController.getSuggestions(task_request)
        return suggestions
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    