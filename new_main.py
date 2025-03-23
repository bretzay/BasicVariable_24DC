import os
from langgraph.prebuilt import create_react_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from pydantic import BaseModel, Field
import requests
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

HOTEL_API_KEY = os.getenv("HOTEL_API_KEY")
HOTEL_BASE_URL = os.getenv("HOTEL_BASE_URL")
header = {"Authorization": f"Token {HOTEL_API_KEY}"}


class Client(BaseModel):
    id: int = Field(..., ge=0, description="Unique identifier for the client", read_only=True)
    name: str = Field(..., max_length=100, description="Name of the client")
    phone_number: str = Field(..., max_length=20, description="Client's phone number")
    room_number: str | None = Field(None, max_length=10, description="Client's room number (optional)")
    special_requests: str | None = Field(None, description="Special requests from the client")



@tool
def PostClient(client: Client):
    """Envoie les données du client à l'API avec la methode POST, renvoie la réponse. Le client ID en paramètre doit au moins avoir une ID, un nom, un numéro de téléphone."""
    return requests.post(HOTEL_BASE_URL+"clients/", header=header, paraams=client)

@tool
def GetClient(client: Client):
    """
    Récupère les données du client depuis l'API en utilisant les données du client en tant que paramètre
    
    Args:
        client: A Client object containing id, name, phone_number, and optional fields.
    
    Returns:
        A string with the API response or an error message.
    """
    params = {"name":client.name}
    try:
        response = requests.get(HOTEL_BASE_URL+"clients/", header=header, params=params)
        if response.status_code == 200:
            # Assuming the API returns a JSON object or list with client data
            data = response.json()
            if isinstance(data, list):
                # If the API returns a list, assume the first match (adjust as needed)
                if data:
                    return f"Client found with ID: {data[0]['id']}"
                else:
                    raise ValueError("No client found with that name")
            elif isinstance(data, dict):
                # If the API returns a single client object
                return f"Client found with ID: {data['id']}"
            else:
                    raise ValueError("Unexpected response format")
    except requests.RequestException as e:
        return f"Error in request: {str(e)}"
    except ValueError as e:
        return f"Error: {str(e)}"

tools=[GetClient,
       PostClient]
model = ChatMistralAI(model="mistral-large-latest")
memory = MemorySaver()
agent_executor = create_react_agent(model, tools=tools, checkpointer=memory)

config = {"configurable": {"thread_id": "client-thread-123"}}

def run_agent():
    query = input("Quel est votre nom?")
    response = agent_executor.invoke(
        input=HumanMessage(query),
        config=config
    )
    return response["messages"][-1].content
print(run_agent())