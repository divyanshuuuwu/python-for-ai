retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

docs = retriever.invoke("What is the refund policy?")