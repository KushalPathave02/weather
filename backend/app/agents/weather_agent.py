from langgraph.prebuilt import create_react_agent
from langchain_core.tools import Tool

from app.tools.weather_tool import get_weather
from app.llm.ollama_llm import get_llm


def create_weather_agent():
    llm = get_llm()

    tools = [
        Tool(
            name="Weather Tool",
            func=get_weather,
            description="Use this tool to get weather information of a city"
        )
    ]

    agent = create_react_agent(llm, tools)

    return agent
