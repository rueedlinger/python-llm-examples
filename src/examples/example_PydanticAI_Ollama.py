from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class CityLocation(BaseModel):
    city: str
    country: str


def get_city_location(model_id: str, query: str):
    ollama_model = OpenAIModel(
        model_name=model_id, provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    )
    agent = Agent(ollama_model, output_type=CityLocation)
    result = agent.run_sync(query)
    return result



if __name__ == "__main__":
    models = ["llama3.2:1b", "llama3.2:3b", "llama3.3"]
    
    query = 'Where were the olympics held in 2012?'
    
    for model in models:
        result = get_city_location(model, query)
        print(result.output)
        print(result.usage())

