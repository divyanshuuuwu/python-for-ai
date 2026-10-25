from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

prompt = ChatPromptTemplate.from_template(
    "Return three programming languages as JSON "
    "with a key named languages.\n"
    "Question: {question}"
)

parser = JsonOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "question": "Name three popular programming languages."
})

print(result)
print(result["languages"])