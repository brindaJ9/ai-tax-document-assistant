from src.rag import build_rag_pipeline, answer_question


pdf_path = "data/income_tax_act_2025.pdf"


# Build the retrieval system
model, index, chunks = build_rag_pipeline(pdf_path)

print(f"Created {len(chunks)} chunks.")


# Ask a question
question = "Who is the current Prime Minister of India?"# Run the RAG pipeline
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


# Display the sources retrieved
print("\nSources:\n")

for chunk in retrieved_chunks:
    print(f"Page {chunk['page']}")
    print("-" * 40)