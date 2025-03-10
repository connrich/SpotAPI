# Local system interaction
import os
from dotenv import load_dotenv

# HTTPS Request
import requests

if __name__ == "__main__":
    load_dotenv()

    client_id = os.getenv('CLIENT_ID')
    client_id_secret = os.getenv('CLIENT_ID_SECRET')
    response = requests.post("https://accounts.spotify.com/api/token", 
                            headers={'Content-Type': 'application/x-www-form-urlencoded'},
                            data=f'grant_type=client_credentials&client_id={client_id}&client_secret={client_id_secret}')
    
    print(response.json()['access_token'])