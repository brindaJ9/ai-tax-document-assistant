from src.rag import build_rag_pipeline, answer_question
from src.citations import get_cited_sources

pdf_path = "data/income_tax_act_2025.pdf"


# Build the retrieval system
model, index, chunks = build_rag_pipeline(pdf_path)

print(f"Created {len(chunks)} chunks.")


# Ask a question
question = "According to Section 92, what is included under income from other sources?"

#Run the RAG pipeline
answer, retrieved_chunks = answer_question(
    question,
    model,
    index,
    chunks,
    k=3
)


# Display the answer
print("\nAnswer:\n")
print(answer)


# Format the retrieved sources
sources = get_cited_sources(
    answer,
    retrieved_chunks
)

print("\nSources:\n")

for source in sources:
    print(
        f"• Source {source['source_number']} — "
        f"Income-tax Act, 2025 — Page {source['page']}"
    )