import os
from mistralai import Mistral
var=input("Avez-vous des question ?")
agent_id_key=""
api_key = ""    #os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id=agent_id_key,
    messages=[
        {
            "role": "user",
            "content": var,
        },
    ],
)
print(chat_response.choices[0].message.content)