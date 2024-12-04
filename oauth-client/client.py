import os
import requests

def get_access_token():
    url = os.getenv('TOKEN_URL')
    client_id = os.getenv('CLIENT_ID')  # Read from environment variable
    client_secret = os.getenv('CLIENT_SECRET')
    scopes = os.getenv('SCOPES')
    response = requests.post(
        url,
        data={"grant_type": "client_credentials", "scope": scopes},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]

url = os.getenv('TOKEN_URL')
print(f"token url: {url}")
ctx = os.getenv('API_CONTEXT')
print(f"api ctx: {ctx}")
client_id = os.getenv('CLIENT_ID')
print(f"client id: {client_id}")


access_token = get_access_token()
print(f"access token: {access_token}")

# invoke an API with the access token
url = os.getenv('API_URL')
print(f"api url: {url}")

url += ctx

response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
print(f"response status: {response.status_code}")
print(f"response payload: {response.text}")
