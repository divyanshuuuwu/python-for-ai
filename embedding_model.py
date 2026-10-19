import langchain_openai
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

llm = langchain_openai.OpenAI(temperature=0.0)

chain = langchain_openai.OpenAIEmbeddingsChain.from_llm(llm, embeddings)        

print(chain.run("What is the capital of France?"))  