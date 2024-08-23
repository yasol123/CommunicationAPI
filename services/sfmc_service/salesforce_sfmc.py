import requests
from .api_client_interface import APIClientInterface
from config.settings import settings

class SFMCClient(APIClientInterface):
    def __init__(self, auth_url: str, api_base_url: str, client_id: str, client_secret: str, resource_id: str):
        self.auth_url = auth_url
        self.api_base_url = api_base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.resource_id = resource_id
        self.access_token = None

    def authenticate(self):
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.auth_url, data=payload)
        response.raise_for_status()
        self.access_token = response.json().get('access_token')

    def make_api_request(self, endpoint: str, method: str = 'GET', data: dict = None) -> dict:
        if not self.access_token:
            self.authenticate()
        
        url = f"{self.api_base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
