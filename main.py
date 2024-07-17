import requests
import json
import time
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

class DrillbitAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.jwt_token = None
        self.jwt_expiry = 0

    def authenticate(self, username, password):
        url = f"{self.base_url}/authentication/authenticate"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            # Extract JWT and other data from response
            response_data = response.json()
            self.jwt_token = response_data['token']
            self.jwt_expiry =  jwt.decode(self.jwt_token, options={"verify_signature": False})['exp']

            print("Authentication successful.")
            print(f"JWT token: {self.jwt_token}")
            print(f"Expires at: {time.ctime(self.jwt_expiry)}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to authenticate: {e}")
            print(response.json())
    def is_token_valid(self):
        if self.jwt_token is None or self.jwt_expiry < time.time():
            return False
        return True

    def create_folder(self, folder_name):
        url = f"{self.base_url}/pro/folder"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.jwt_token}'
        }
        data = {
                "folder_name": folder_name,
                "exclude_reference": "NO",
                "exclude_quotes": "NO",
                "exclude_small_sources": "yes",
                "grammar_check": "NO",
                "db_studentpaper": "YES",
                "db_publications": "YES",
                "db_internet": "YES",
                "institution_repository": "YES",
                "exclude_phrases": "YES",
                "phrases": {
                    "p1": "phrases 1",
                    "p2": "phrases 2",
                    "p3": "Phrases 3"
                }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            # Process response
            response_data = response.json()
            status = response_data['status']
            message = response_data['message']
            timestamp = response_data['timeStamp']

            print(f"Folder creation status: {status}")
            print(f"Message: {message}")
            print(f"Timestamp: {timestamp}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to create folder: {e}")

if __name__ == "__main__":
    base_url = "https://s1.drillbitplagiarismcheck.com"
    api = DrillbitAPI(base_url)

    username = os.getenv("DRILLBIT_USERNAME") 
    password = os.getenv("DRILLBIT_PASSWORD") 
    print(username, password)
    api.authenticate(username, password)

    if api.is_token_valid():
        folder_name = "Pro folder"
        api.create_folder(folder_name)
    else:
        print("Unable to proceed, authentication failed.")

