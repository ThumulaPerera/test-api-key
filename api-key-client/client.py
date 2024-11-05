import os
import requests

# invoke an API with the access token
url = os.getenv('API_URL')
print(f"api url: {url}")
api_key = os.getenv('API_KEY')
print(f"api key: {api_key}")

url += "/greeting?name=John"

response = requests.get(url, headers={"choreo-api-key": f"{api_key}"})
print(f"response status: {response.status_code}")
print(f"response payload: {response.text}")