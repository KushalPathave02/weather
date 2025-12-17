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

## Model Selection: Mistral vs. LLaMA-3

During development, we initially used the `llama3` model from Ollama. However, we encountered a critical issue that prevented the application from functioning correctly.

### The Problem with `llama3`

The core of this application relies on a LangChain agent's ability to use tools. This capability is known as **tool-calling** or **function-calling**. When the agent receives a query like "what is the weather in Pune?", the LLM needs to understand that it should use the `weather_tool` to get the answer.

The specific version of `llama3` available through Ollama at the time of development **does not support tool-calling**. When our LangChain agent attempted to use the `weather_tool`, the `llama3` model rejected the request, resulting in a `400 Bad Request` error from the Ollama server with the message:

```
ollama._types.ResponseError: registry.ollama.ai/library/llama3:latest does not support tools
```

This is a limitation of the model itself, not a bug in our code.

### The Solution: Switching to `mistral`

To resolve this issue, we switched to the `mistral` model.

**Why `mistral`?**

*   **Tool-Calling Support**: `mistral` is a powerful model that fully supports tool-calling, making it compatible with LangChain agents.
*   **Performance**: It provides a great balance of performance and resource requirements for local development.
*   **Compatibility**: It works seamlessly with our existing architecture without requiring any significant code refactoring.

By simply changing the model name in our backend configuration from `llama3` to `mistral`, we were able to resolve the error and create a fully functional weather agent.
