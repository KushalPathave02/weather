from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import create_weather_agent

router = APIRouter()
# Create the weather agent instance
agent = create_weather_agent()

class ChatRequest(BaseModel):
    message: str

PERSON_CITY_MAP = {
    "virat kohli": "mumbai",
    "sachin tendulkar": "mumbai",
    "narendra modi": "new delhi"
}

def is_weather_question(text: str) -> bool:
    weather_keywords = [
        "weather",
        "temperature",
        "temp",
        "cold",
        "hot",
        "heat",
        "rain",
        "raining",
        "climate",
        "forecast",
        "humidity",
        "wind",
        "cool",
        "warm",
        "chilly"
    ]
    text = text.lower()
    return any(word in text for word in weather_keywords)

@router.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message.lower()

    if not is_weather_question(user_input):
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

    # resolve person → city
    for person, city in PERSON_CITY_MAP.items():
        if person in user_input:
            user_input = f"weather in {city}"

    result = agent.invoke({"input": user_input})
    return {"response": result["output"]}
