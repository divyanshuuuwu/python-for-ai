
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a framework for building applications powered by large language models.
It provides tools for creating AI agents, RAG systems, and chatbots.

RAG stands for Retrieval-Augmented Generation.
It allows an AI model to retrieve relevant information from external documents
before generating an answer.

Text splitting is an important step in RAG.
Large documents are divided into smaller chunks so that relevant information
can be retrieved efficiently.
"""

# Create the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

# Split the text into chunks
chunks = splitter.split_text(text)

# Print each chunk
for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)
