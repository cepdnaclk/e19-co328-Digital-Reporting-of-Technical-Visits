from pydantic import BaseModel
from typing import List, Dict

class TaskRequest(BaseModel):
    task_title: str
    description: str

class TechnicianSuitability(BaseModel):
    technician_id: str
    suitability: float

