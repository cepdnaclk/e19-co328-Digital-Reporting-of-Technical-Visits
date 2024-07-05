from models.suggestModel import TaskRequest, TechnicianSuitability
from ai_component.find_matches import find_top_matches

def getSuggestions(task_request: TaskRequest):

    task = {
        'description': task_request.description
    }
    
    technician_list = [
        {'id': 'T001', 'description': 'Repair the broken sprinkler system in the garden.'},
        {'id': 'T002', 'description': 'Fix the broken sprinkler system in the garden.'},
        {'id': 'T003', 'description': 'Replace the broken sprinkler system in the garden.'},
        {'id': 'T004', 'description': 'Repair the broken sprinkler system in the garden.'},
        {'id': 'T005', 'description': 'Fix the broken sprinkler system in the garden.'},
    ]

    task_updated = find_top_matches(task, technician_list)

    # Create response
    response = [
        {"technician_id": technician_id, "suitability": round(float(suitability)*100, 2)}
        for technician_id, suitability in task_updated['matches']
    ]
    
    # Return only the top 3 suitable technicians
    return response
