import time
import json
import requests

# class ApiRequest:
def get_random():
    """
    Returns a random Chuck Norris joke.
    """
    random_chuck_jokes = "https://api.chucknorris.io/jokes/random"
    response = requests.get(random_chuck_jokes)
    json_data = json.loads(response.text)
    
    return json_data

def find_specific(query):
    """
    Returns a list of Chuck Norris jokes that match the query.
    """
    query_chuck_jokes = "https://api.chucknorris.io/jokes/search?query=" + query
    response = requests.get(query_chuck_jokes)
    json_data = json.loads(response.text)
    
    return json_data

while True:
    new_request = get_random()
    print(new_request)
    time.sleep(10)
