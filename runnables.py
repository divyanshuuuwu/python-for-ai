from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

model = ChatOpenAI(model="gpt-4o-mini")

response = prompt.invoke({"topic": "RAG"})

print(response)