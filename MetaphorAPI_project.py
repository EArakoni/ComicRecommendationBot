from metaphor_python import Metaphor
api_key = "a8ed57b5-a41c-4308-8fc8-a0d20e582077"
metaphor = Metaphor(api_key)

#Specifications of what I'm looking for
def get_comic_recommendations(user_preferences):
    # Use the Metaphor API to search for DC comics based on user preferences
    query = 'Popular Comics'
    options = {
        'type': 'neural',  # To get high-quality content
        'num_results': 10  # Number of results you want
    }
    search_response = metaphor.search(query, **options)

    # Display recommended comics to the user
    if not search_response.results:
        return "Sorry, no comics found based on your preferences."

    recommendations = []
    for result in search_response.results:
        comic_info = {
            "Title": result.title,
            "URL": result.url,
            "Published Date": result.published_date,
            "Author": result.author,
            "Extract": result.extract,
        }
        recommendations.append(comic_info)

    return recommendations

def main():
    print("Welcome to the Comic Recommendation Bot!")
    
    # Collect user preferences
    user_preferences = input("Tell me what superhero you'd like me to find comics for: ")
    # Get comic recommendations based on user preferences
    recommendations = get_comic_recommendations(user_preferences)

    if isinstance(recommendations, list):
        print("\nHere are some DC comics recommendations for you:")
        for idx, comic_info in enumerate(recommendations, start=1):
            print(f"\nRecommendation {idx}:")
            for key, value in comic_info.items():
                print(f"{key}: {value}")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()
