import operator
import os
import requests
from typing import Annotated, Optional, Sequence
from typing_extensions import TypedDict
from langchain.agents import AgentExecutor, create_tool_calling_agent
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import asyncio
from langgraph.graph import END, StateGraph, START
from langchain.chat_models import init_chat_model

HOTEL_API_KEY = os.getenv("HOTEL_API_KEY")

model = ChatMistralAI(model_name="mistral-large-latest")
llm = init_chat_model("mistral-large-latest", model_provider="mistralai")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
"""Vous êtes un assistant hôtelier qui aide les clients de l'hotel californian hotel au Mans.
Vous n'êtes pas supposé répondre à des questions qui n'ont aucun rapport avec l'hotel ou les activités annexes
S'il vous manque une information, demandez la au client afin de répondre à son besoin

Use fetch_restaurant for information about restaurant.
Use fetch_meal for information about meal time.
Use fetch_reservation for information about client's reservation.
Use fetch_spas for information about spas
""",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

@tool(description="Donne une liste des restaurants pour que l'utilisateur ai des informations à leur sujets.")
def fetch_restaurant():
    api_url = "https://app-584240518682.europe-west9.run.app/api/restaurants/"
    headers = {"Authorization": f"Token {HOTEL_API_KEY}"}
    try:
        response = requests.get(headers=headers, url=api_url)
        response.raise_for_status()
        time.sleep(0.3)
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la récupération : {e}"

@tool(description="Donne le nom des différents types de repas à l'utilisateur")
def fetch_meal():
    api_url = "https://app-584240518682.europe-west9.run.app/api/meals/"
    headers = {"Authorization": f"Token {HOTEL_API_KEY}"}
    try:
        response = requests.get(headers=headers, url=api_url)
        response.raise_for_status()
        time.sleep(0.3)
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la récupération : {e}"

@tool(description="Donne la liste des spas disponibles pour l'utilisateur")
def fetch_spas():
    api_url = "https://app-584240518682.europe-west9.run.app/api/spas/"
    headers = {"Authorization": f"Token {HOTEL_API_KEY}"}
    try:
        response = requests.get(headers=headers, url=api_url)
        response.raise_for_status()
        time.sleep(0.3)
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la récupération : {e}"


from typing import Optional
from pydantic import BaseModel, Field

# Pydantic
class User(BaseModel):
    """Information about the user."""

    id: Optional[int] = Field(description="id of the user in the hotel")
    name: str = Field(description="The name of the client")
    phone_number: str = Field(description="the phone number of the client")
    room_number: str = Field(description="The room number of the client")

structured_llm = llm.with_structured_output(User)


@tool(description="Donne des informations au sujet de la réservation de l'utilisateur aux restaurants.")
def fetch_reservation() -> str:
    api_url = "https://app-584240518682.europe-west9.run.app/api/reservations/"
    headers = {"Authorization": f"Token {HOTEL_API_KEY}"}
    try:
        response = requests.get(headers=headers, url=api_url)
        response.raise_for_status()
        time.sleep(0.3)
        return str(response.json())
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la récupération : {e}"

tools=[fetch_meal, fetch_reservation, fetch_restaurant]

agent = create_tool_calling_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def run_conversation():
    while True:
        chat_history = []
        initial_input = input()
        response = agent_executor.invoke({
            "input": initial_input,
            "chat_history": chat_history
        })
        print(f"{response['output']}")
        chat_history.append(HumanMessage(content=initial_input))
        chat_history.append(AIMessage(content=response["output"][-1]))
        time.sleep(1)
print("Comment puis-je vous aider?")
run_conversation()