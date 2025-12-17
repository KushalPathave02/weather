from langchain_ollama import ChatOllama

# Trigger reload
def get_llm():
    """Initializes and returns the Ollama LLM instance."""
    return ChatOllama(
        model="mistral",
        temperature=0.2
    )
