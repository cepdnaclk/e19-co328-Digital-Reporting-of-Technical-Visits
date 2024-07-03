from models.suggestModel import TaskRequest, TechnicianSuitability
from ai_component.find_matches import find_top_matches

def getSuggestions(task_request: TaskRequest):
    
    technician_list = [
        "string to compare with example",
        "another different example string",
        "completely unrelated text",
        "example string match test",
        "yet another example string",
        "another example string different"
    ]

    top_matches = find_top_matches(task_request.description, technician_list)

    # Create response
    response = [
        {"technician_id": technician_list[technician_id], "suitability": round(float(suitability)*100, 2)}
        for technician_id, suitability in top_matches
    ]
    
    # Return only the top 3 suitable technicians
    return response
