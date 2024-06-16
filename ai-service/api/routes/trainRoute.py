from fastapi import APIRouter, HTTPException
from models.suggestModel import TaskRequest, TechnicianSuitability
from typing import List, Dict

router = APIRouter()

@router.post("/mini-train-technician", response_model=List[TechnicianSuitability])
async def suggest_technician_to_task(task_request: TaskRequest):
    # This is a mock response. In a real application, you would have logic here to determine the suitability.
    mock_response = [
        {"technician_id": "T001", "suitability": 85.1},
        {"technician_id": "T002", "suitability": 65.3},
        {"technician_id": "T003", "suitability": 55.1},
    ]
    
    try:
        
        return mock_response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))