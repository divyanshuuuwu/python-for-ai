from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain helps developers build applications powered by language models.

RAG stands for Retrieval-Augmented Generation.
It retrieves relevant information before generating an answer.

Text splitters divide large documents into smaller chunks.
These chunks can then be converted into embeddings.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print()