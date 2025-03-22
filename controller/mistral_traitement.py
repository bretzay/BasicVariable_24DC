import os
import json
import requests
from dotenv import load_dotenv
from mistralai import Mistral
load_dotenv()

#var=input("Avez-vous des question ?")



api_key = os.getenv("MISTRAL_API_KEY")
agent_json_id = os.getenv("MISTRAL_AGENT_JSON_ID")

client = Mistral(api_key=api_key)





