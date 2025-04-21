from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from typing import List, Optional


class Result(BaseModel):
    """Result class for the agent."""
    countries: List[str] = []


def get_countries(model_id: str, query: str):
    ollama_model = OpenAIModel(
        model_name=model_id,
        provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
    )
    agent = Agent(
        model=ollama_model,
        output_type=Result,
        retries=5,
        system_prompt=(
            "You are a helpful AI assistant. "
            "You will be given a a text and you need to extract the countries from it. "            
        ),
    )
    result = agent.run_sync(query)
    return result


if __name__ == "__main__":
    models = ["llama3.2:1b", "llama3.2:3b", "llama3.3"]

    prompt = "I love programming. I have been to France, Germany, and Japan. I also want to visit Brazil and Argentina."
    #prompt = "I love programming."

    for model in models:
        try:
            print(f"Testing model: {model}")
            result = get_countries(model, prompt)
            print("result:", result.output)            
        except Exception as e:
            print(f"Error with model {model}: {e}")
