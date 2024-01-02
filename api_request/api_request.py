import json
import requests

class ApiRequest:
    def get_random(self):
        random_chuck_jokes = "https://api.chucknorris.io/jokes/random"
        response = requests.get(random_chuck_jokes)
        json_data = json.loads(response.text)
        
        return json_data
    
    def find_specific(self, query):
        query_chuck_jokes = "https://api.chucknorris.io/jokes/search?query=" + query
        response = requests.get(query_chuck_jokes)
        json_data = json.loads(response.text)
        
        return json_data
