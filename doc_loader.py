from langchain_core.documents import Document

doc = Document(
    page_content="Our company provides 20 days of paid leave.",
    metadata={
        "source": "employee_policy.pdf",
        "department": "HR"
    }
)

print(doc.page_content)
print(doc.metadata)