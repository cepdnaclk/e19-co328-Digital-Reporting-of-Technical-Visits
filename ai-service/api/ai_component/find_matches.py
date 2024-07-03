from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_top_matches(target_string, string_list, top_n=3):
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


if __name__ == '__main__':
    # Example usage
    target_string = "example string to match"
    string_list = [
        "string to compare with example",
        "another different example string",
        "completely unrelated text",
        "example string match test",
        "yet another example string",
        "another example string different"
    ]

    top_matches = find_top_matches(target_string, string_list)
    for match, score in top_matches:
        print(f"Match: {string_list[match]}, Score: {score}")
