# AI Weather Assistant - Backend

This directory contains the backend code for the AI Weather Assistant, built with FastAPI and LangChain.

## Setup and Running

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Ollama LLM:**
    Make sure you have Ollama installed and the `llama3` model pulled.
    ```bash
    ollama run llama3
    ```

3.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.
