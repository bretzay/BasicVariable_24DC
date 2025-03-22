import os
from dotenv import load_dotenv
from mistralai import Mistral
var=input("Avez-vous des question ?")

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
agent_id = os.getenv("MISTRAL_AGENT_ID")

client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id=agent_id,
    messages=[
        {
            "role": "user",
            "content": var,
        },
    ],
)
print(chat_response.choices[0].message.content)