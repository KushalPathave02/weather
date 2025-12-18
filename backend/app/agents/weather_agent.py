from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool

from app.tools.weather_tool import get_weather
from app.llm.ollama_llm import get_llm


def create_weather_agent():
    llm = get_llm()

    tools = [
        Tool(
            name="get_weather",
            func=get_weather,
            description="Use this tool to get weather information for a specific city.",
        )
    ]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that provides weather information."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor
