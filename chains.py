from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple language."
)

# 2. Initialize the model
model = ChatOpenAI(model="gpt-4.1-mini")

# 3. Create an output parser
parser = StrOutputParser()

# 4. Connect everything into a chain
chain = prompt | model | parser

# 5. Execute the chain
response = chain.invoke({"topic": "RAG"})

print(response)