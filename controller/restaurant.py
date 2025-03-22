# presenters/restaurant_presenter.py
import requests
from model.restaurant import Restaurant
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
BASE_URL = os.getenv("HOTEL_BASE_URL")  # Replace with real URL from hackathon
API_KEY = os.getenv("HOTEL_API_KEY")  # Ensure this is set in .env




def get_all_restaurants(page: int = 1) -> list[Restaurant]:
    """
    Fetch a list of restaurants from the hotel API.
    Args:
        page (int): Page number for paginated results (default: 1).
    Returns:
        list[Restaurant]: List of Restaurant objects.
    Raises:
        requests.HTTPError: If the API call fails.
    """
    headers = {"Authorization": f"Token {API_KEY}"}
    params = {"page": page} if page > 1 else {}  # Only add page param if needed
    response = requests.get(f"{BASE_URL}/restaurants/", headers=headers, params=params)
    response.raise_for_status()  # Raise exception on 4xx/5xx errors
    
    data = response.json()
    # Extract restaurants from the "results" field of the paginated response
    return [Restaurant(**restaurant_data) for restaurant_data in data["results"]]

# Optional: Function to handle pagination metadata if needed later
def get_restaurants_paginated(page: int = 1) -> tuple[list[Restaurant], int, str, str]:
    headers = {"Authorization": f"Token {API_KEY}"}
    params = {"page": page} if page > 1 else {}
    response = requests.get(f"{BASE_URL}/api/restaurants/", headers=headers, params=params)
    response.raise_for_status()
    
    data = response.json()
    restaurants = [Restaurant(**restaurant_data) for restaurant_data in data["results"]]
    return restaurants, data["count"], data["next"], data["previous"]