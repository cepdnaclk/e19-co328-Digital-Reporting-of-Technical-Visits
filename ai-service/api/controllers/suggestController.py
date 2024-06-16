from models.suggestModel import TaskRequest, TechnicianSuitability
import joblib
import numpy as np

# Load the model, vectorizer, and label encoder
model = joblib.load('ai-models/random_forest_model.joblib')
vectorizer = joblib.load('ai-models/tfidf_vectorizer.joblib')
label_encoder = joblib.load('ai-models/label_encoder.joblib')

def getSuggestions(task_request: TaskRequest):
    # Prepare input data for prediction
    input_data = [task_request.description + " " + task_request.task_title]
    X_input = vectorizer.transform(input_data)
    
    # Get probabilities for each technician
    probabilities = model.predict_proba(X_input)[0]
    
    # Get sorted list of technicians based on suitability
    technician_ids_encoded = np.argsort(-probabilities)
    suitability_scores = np.sort(probabilities)[::-1]

    # Decode technician IDs
    technician_ids = label_encoder.inverse_transform(technician_ids_encoded)

    # Create response
    response = [
        {"technician_id": technician_id, "suitability": float(suitability)}
        for technician_id, suitability in zip(technician_ids, suitability_scores)
    ]
    
    # Return only the top 3 suitable technicians
    return response[:3]