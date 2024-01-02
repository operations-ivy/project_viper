import requests

response = requests.get('https://1.1.1.1/cdn-cgi/trace')

print(type(response))
print(response.text)