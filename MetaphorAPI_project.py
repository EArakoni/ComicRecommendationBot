from metaphor_python import Metaphor
api_key = "a8ed57b5-a41c-4308-8fc8-a0d20e582077"
metaphor = Metaphor(api_key)
#Specifications of what I'm looking for


query = 'Batman Multiverse comics'
options = {
    'type': 'neural' ,
    'num_results': 10
}

search_response = metaphor.search(query, **options)
    
for idx, result in enumerate(search_response.results, start=1):
    print(f"Result {idx}:")
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Published Date: {result.published_date}")
    print(f"Author: {result.author}")
    print(f"Extract: {result.extract}")
    print()
