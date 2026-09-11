from src.retriever import build_retriever, retrieve


pdf_path = "data/income_tax_act_2025.pdf"


# Build the retrieval system
model, index, chunks = build_retriever(pdf_path)

print(f"Created {len(chunks)} chunks.")


# Ask a question
query = "What types of income are taxable under income from other sources?"


# Retrieve relevant chunks
results = retrieve(
    query,
    model,
    index,
    chunks,
    k=3
)


# Display results
print("\nTop results:\n")

for result in results:
    print(f"Page: {result['page']}")
    print(f"Distance: {result['distance']:.4f}")
    print(result["text"][:500])
    print("-" * 60)