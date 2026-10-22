from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = ChatPromptTemplate.from_template(
    "Extract the person's information from the text.\n"
    "{format_instructions}\n"
    "Text: {text}"
).partial(
    format_instructions=parser.get_format_instructions()
)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

chain = prompt | llm | parser

result = chain.invoke({
    "text": "Rahul is 22 years old."
})

print(result.name)
print(result.age)