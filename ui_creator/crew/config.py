import os
from crewai import LLM

def get_api_keys():
    return {
        "openai": os.getenv("OPENAI_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "google": os.getenv("GEMINI_API_KEY"),
        "openrouter": os.getenv("OPENROUTER_API_KEY")
    }

def select_llm(provider):
    if provider.lower() == "openai":
        return LLM(
            model=os.getenv("OPENAI_MODEL_NAME", "openai/gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif provider.lower() == "anthropic":
        return LLM(
            model=os.getenv("ANTHROPIC_MODEL_NAME", "anthropic/claude-3-7-sonnet-latest"),
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
    elif provider.lower() == "google":
        return LLM(
            model=os.getenv("GOOGLE_MODEL_NAME", "gemini/gemini-2.0-flash"),
            api_key=os.getenv("GEMINI_API_KEY")
        )
    elif provider.lower() == "openrouter":
        return LLM(
            model=os.getenv("OPENROUTER_MODEL_NAME", "openrouter/qwen/qwq-32b:free"),
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
