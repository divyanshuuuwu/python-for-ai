from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

# 1. Create the embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# 2. Create the vector store
vector_store = InMemoryVectorStore(embeddings)

# 3. Add documents
documents = [
    Document(
        page_content="Employees get 20 days of annual leave."
    ),
    Document(
        page_content="Employees receive health insurance."
    ),
    Document(
        page_content="The office is open from 9 AM to 6 PM."
    ),
]

vector_store.add_documents(documents)

# 4. Search for relevant information
results = vector_store.similarity_search(
    "How many vacation days do employees get?",
    k=2
)

# 5. Print the retrieved documents
for doc in results:
    print(doc.page_content)