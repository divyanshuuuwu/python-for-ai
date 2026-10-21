from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI tutor who explains concepts simply."),
    ("human", "Explain {topic} with an example.")
])

messages = prompt.format_messages(topic="Embeddings")

for message in messages:
    print(message)