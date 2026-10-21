
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


# Step 1: Define the output structure
class Person(BaseModel):
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")
    profession: str = Field(description="Person's profession")


# Step 2: Initialize the model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


# Step 3: Enable structured output
structured_model = model.with_structured_output(Person)


# Step 4: Ask a question
response = structured_model.invoke(
    "Extract the person's information: "
    "Rahul is 25 years old and works as a software engineer."
)


# Step 5: Print the result
print(response)
print(response.name)
print(response.age)
print(response.profession)
