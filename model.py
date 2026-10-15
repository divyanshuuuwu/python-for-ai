#models in langchain






from langchain_openai import ChatOpenAI

# 1. Create the model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# 2. Send a message to the model
response = model.invoke("What is RAG in AI?")

# 3. Print the AI's response
print(response.content)
