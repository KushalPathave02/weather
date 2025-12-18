import requests
from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import create_weather_agent

router = APIRouter()
agent = create_weather_agent()

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"

class ChatRequest(BaseModel):
    message: str

PERSON_CITY_MAP = {
    "virat kohli": "mumbai",
    "sachin tendulkar": "mumbai",
    "narendra modi": "new delhi"
}

def is_city(text: str) -> bool:
    """Check if a string is a valid city by calling the geocoding API."""
    try:
        response = requests.get(GEOCODING_API_URL, params={"name": text, "count": 1})
        response.raise_for_status()
        return bool(response.json().get("results"))
    except requests.exceptions.RequestException:
        return False

def is_weather_question(text: str) -> bool:
    weather_keywords = [
        "weather", "temperature", "temp", "cold", "hot", "heat", "rain",
        "raining", "climate", "forecast", "humidity", "wind", "cool", "warm", "chilly"
    ]
    return any(word in text.lower() for word in weather_keywords)

@router.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message.lower()
    is_weather_prompt = is_weather_question(user_input)

    # Handle person-to-city mapping first
    for person, city in PERSON_CITY_MAP.items():
        if person in user_input:
            if is_weather_prompt:
                user_input = f"weather in {city}"
                break 
    
    # Re-evaluate after potential mapping
    is_weather_prompt = is_weather_question(user_input)

    # If it's not a weather question, check if it's a city name
    if not is_weather_prompt and is_city(user_input):
        user_input = f"weather in {user_input}"
    elif not is_weather_prompt:
        return {
            "response": (
                "I can only answer weather-related questions 🌤️\n\n"
                "Try prompts like:\n"
                "• Is it cold in Mumbai today?\n"
                "• Weather of Pune today\n"
                "• Will it rain in Delhi?\n"
                "• Is it hot where Virat Kohli lives?"
            )
        }

    result = agent.invoke({"input": user_input})
    return {"response": result["output"]}
