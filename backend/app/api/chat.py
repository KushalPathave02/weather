from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import create_weather_agent

router = APIRouter()
# Create the weather agent instance
agent = create_weather_agent()

class ChatRequest(BaseModel):
    message: str


# ✅ simple weather intent check
def is_weather_question(text: str) -> bool:
    weather_keywords = [
        "weather",
        "temperature",
        "temp",
        "rain",
        "raining",
        "climate",
        "forecast",
        "humidity",
        "wind"
    ]
    text = text.lower()
    return any(word in text for word in weather_keywords)


@router.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message

    # ❌ non-weather prompt
    if not is_weather_question(user_input):
        return {
            "response": (
                "I can only help with weather-related questions 🌤️\n\n"
                "Please try prompts like:\n"
                "• What is the weather in Pune today?\n"
                "• Temperature in Mumbai\n"
                "• Will it rain in Delhi today?\n"
                "• Weather forecast for Bangalore"
            )
        }

    # ✅ weather prompt → call agent
    result = agent.invoke({"input": user_input})
    return {"response": result["output"]}
