# Weather Agent Project

This project is a full-stack web application that provides weather information through a conversational AI agent. It features a React frontend and a Python backend powered by FastAPI and LangChain.

## Workflow

The application follows a simple client-server architecture:

1.  **Frontend (React + Vite)**: The user interacts with a chat interface built with React. When a user asks a question about the weather (e.g., "what's the weather in Pune?"), the frontend sends a POST request to the backend API.

2.  **Backend (FastAPI)**: The backend receives the request at the `/chat` endpoint.

3.  **Agent (LangChain + Ollama)**:
    *   The backend uses a LangChain agent to process the user's message.
    *   The agent is powered by the `mistral` model running locally via Ollama.
    *   The agent is equipped with a `weather_tool` that can fetch real-time weather data for a given city.

4.  **Tool-Calling**:
    *   The `mistral` model determines that to answer the user's query, it needs to use the `weather_tool`.
    *   The agent executes the tool, which makes an external API call to a weather service to get the data for the specified city.

5.  **Response Generation**:
    *   The weather data is returned to the `mistral` model.
    *   The model uses this data to generate a natural language response (e.g., "The current temperature in Pune is 24°C with clear skies.").

6.  **API Response**: The backend sends this generated response back to the frontend.

7.  **Display**: The frontend displays the agent's response to the user in the chat interface.

## Advanced Intent Handling

The agent has been enhanced with a sophisticated, multi-layered intent-filtering system to create a more intelligent and user-friendly experience. This system ensures that the agent responds appropriately to a wide range of user inputs.

The logic is as follows:

1.  **Expanded Keyword Detection**: The system first checks if the user's prompt contains any weather-related keywords (e.g., "weather," "temperature," "cold," "hot," "rain"). This initial check helps to quickly identify weather-related intent.

2.  **Person-to-City Mapping**: If a weather-related keyword is found, the system then checks for the names of specific individuals (e.g., "Virat Kohli," "Narendra Modi"). If a known person is mentioned, their name is mapped to their city of residence (e.g., "Virat Kohli" → "Mumbai"). The prompt is then rewritten to be a direct weather query for that city (e.g., "weather in Mumbai").

3.  **City-Only Input**: If the prompt does not contain any weather-related keywords, the system makes a call to a geocoding API to determine if the input is a valid city name. If it is, the prompt is reformatted into a direct weather query (e.g., "pune" → "weather in pune").

4.  **Default Response**: If the input is not a weather-related question, does not contain a known person, and is not a valid city, the system returns a default response. This response informs the user of the agent's capabilities and provides examples of supported prompts.

This multi-step process allows the agent to handle a variety of queries, from direct questions to more complex, indirect prompts, while gracefully managing off-topic requests.

## Supported Test Cases

The system has been tested and confirmed to handle the following categories of prompts:

-   **Direct Weather Questions**: Standard questions that explicitly ask for weather information.
    -   "What is the weather in Pune today?"
    -   "Temperature in Mumbai"
    -   "Will it rain in Delhi today?"

-   **Indirect Weather Questions**: Questions that imply a request for weather information without using direct keywords.
    -   "Is it cold where Virat Kohli lives?"
    -   "How hot is it in Sachin Tendulkar’s city?"
    -   "Does it feel warm in New Delhi?"

-   **City-Only Inputs**: Prompts that consist of only a city name.
    -   "Pune"
    -   "Mumbai"
    -   "Delhi"

-   **Non-Weather Questions**: Any prompts that are not related to weather. These are blocked, and a default response is provided.
    -   "Tell me a joke"
    -   "Who is the Prime Minister of India?"
    -   "Explain Artificial Intelligence"

## Technical Decisions

### Model Selection: Ollama's `mistral` vs. `llama3`

During development, we initially used the `llama3` model from Ollama. However, we encountered a critical issue: the version of `llama3` available at the time **did not support tool-calling**. This is a fundamental requirement for our LangChain agent, which needs to use a `weather_tool` to fetch data. Any attempt to use this tool with `llama3` resulted in a `400 Bad Request` error from the Ollama server.

To resolve this, we switched to the `mistral` model, which fully supports tool-calling and integrates seamlessly with our LangChain agent.

### Local Model (Ollama) vs. Cloud API (OpenRouter)

We also considered using OpenRouter, a cloud-based service for accessing various LLMs. However, we faced a similar compatibility issue.

**The Problem with OpenRouter**

The LangChain framework, by default, includes a `tool_choice` field in its API requests to the LLM. The OpenRouter API, at the time of development, did not support this field, which resulted in a `422 Unprocessable Entity` error. While it is possible to customize the LangChain agent to remove this field, it would have required significant code refactoring.

**The Solution: A Local Ollama Model**

By using a locally hosted `mistral` model via Ollama, we achieved full compatibility with LangChain's tool-calling features out-of-the-box. This approach provided a more stable, cost-effective, and controlled environment for development, allowing us to build a robust and reliable weather agent without the need for complex workarounds.
