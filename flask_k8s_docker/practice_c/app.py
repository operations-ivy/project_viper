from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

def get_random():
    """
    Returns a random Chuck Norris joke.
    """
    random_chuck_jokes = "https://api.chucknorris.io/jokes/random"
    response = requests.get(random_chuck_jokes)
    json_data = json.loads(response.text)
    
    return json_data

@app.route('/')
def hello_world():
    return jsonify({
      'greeting': 'Hello World!' 
    })

@app.route('/joke')
def joke():
    new_joke = get_random()
    return jsonify({
      'new joke': new_joke
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')