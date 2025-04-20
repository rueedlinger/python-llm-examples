from langchain_ollama import ChatOllama


def get_response(prompt: str, model: str = "llama3.3"):
    llm = ChatOllama(
        base_url="http://localhost:11434",
        model=model,
        temperature=0.8,
        num_predict=256,
    )

    messages = [
        ("system", "You are a helpful AI assistant."),
        ("human", prompt),
    ]

    response = llm.invoke(messages)
    return response.content


# Example usage
if __name__ == "__main__":

    models = ["llama3.2:1b", "llama3.2:3b", "llama3.3"]

    for model in models:
        response = get_response("I love programming.", model=model)
        print(response)
