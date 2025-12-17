from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.weather_agent import create_weather_agent

router = APIRouter()

agent = create_weather_agent()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    input_data = {"messages": [{"role": "user", "content": req.message}]}
    result = agent.invoke(input_data)
    response = result["messages"][-1].content
    return {"response": response}
