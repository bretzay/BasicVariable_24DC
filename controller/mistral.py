import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
agent_id = os.getenv("MISTRAL_AGENT_ID")

client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id=agent_id,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ],
)
print(chat_response.choices[0].message.content)