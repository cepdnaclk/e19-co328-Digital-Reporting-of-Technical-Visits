from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_top_matches_strings(target_string, string_list, top_n=3):
    # Combine the target string with the list of strings
    combined_strings = [target_string] + string_list
    
    # Convert strings to TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(combined_strings)
    
    # Calculate cosine similarities
    cosine_similarities = cosine_similarity(vectorizer[0:1], vectorizer).flatten()
    
    # Get the top N matches (excluding the first element which is the target string itself)
    similar_indices = cosine_similarities.argsort()[::-1][1:top_n + 1]
    
    # Ensure indices do not go out of range
    similar_strings = [(i-1, cosine_similarities[i]) for i in similar_indices]

    return similar_strings

def find_top_matches(task, technians, top_n=3):

    task_description = task['description']

    technians_descriptions = [technians['description'] for technians in technians]

    match_ids = find_top_matches_strings(task_description, technians_descriptions, top_n)

    match_technians = [(technians[i]['id'], score) for i, score in match_ids]

    task['matches'] = match_technians

    return task

if __name__ == '__main__':
    # Example usage
    task = {'id': 'TS001', 'description': 'Fix the broken sprinkler system in the garden.'}

    technician_list = [
        {'id': 'T001', 'description': 'Repair the broken sprinkler system in the garden.'},
        {'id': 'T002', 'description': 'Fix the broken sprinkler system in the garden.'},
        {'id': 'T003', 'description': 'Replace the broken sprinkler system in the garden.'},
        {'id': 'T004', 'description': 'Repair the broken sprinkler system in the garden.'},
        {'id': 'T005', 'description': 'Fix the broken sprinkler system in the garden.'},
    ]

    task_updated = find_top_matches(task, technician_list)

    for match, score in task_updated['matches']:
        print(f"Match: match, Score: {score}")
