import os
import json
import requests
from dotenv import load_dotenv
from mistralai import Mistral

url ="https://app-584240518682.europe-west9.run.app/api/"
token=os.getenv("NOTRE_TOKEN")
headers = {
    "Authorization": f"{token}"
}
#var=input("Avez-vous des question ?")

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
agent_json_id = os.getenv("MISTRAL_AGENT_JSON_ID")

client = Mistral(api_key=api_key)

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parser la réponse JSON
    data = response.json()
    print(data)
else:
    print(f"Erreur lors de la requête : {response.status_code}")

