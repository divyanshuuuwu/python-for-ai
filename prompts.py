import langchain_core.prompts as prompts


def get_prompt(prompt_type, input_variables):
    if prompt_type == "prompt":
        return prompts.PromptTemplate(
            input_variables=input_variables,
            template="What is a good name for a company that makes {product}?",
        )
    elif prompt_type == "chat":
        return prompts.ChatPromptTemplate.from_messages(
            [
                prompts.SystemMessagePromptTemplate.from_template(
                    "You are a helpful assistant that translates English to French."
                ),
                prompts.HumanMessagePromptTemplate.from_template("{input}"),
            ]
        )
    else:
        raise ValueError(f"Invalid prompt type: {prompt_type}")  # Add more prompt types as needed