from src.document_processor import extract_text_from_pdf, create_chunks
from src.embeddings import load_embedding_model
from src.vector_store import create_faiss_index, search_faiss


# 1. Extract text
pdf_path = "data/income_tax_act_2025.pdf"
pages = extract_text_from_pdf(pdf_path)

# 2. Create chunks
chunks = create_chunks(pages)

print(f"Created {len(chunks)} chunks.")

# 3. Load embedding model
model = load_embedding_model()

# 4. Create embeddings for every chunk
texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(texts)

print(f"Embedding shape: {embeddings.shape}")

# 5. Create FAISS index
index = create_faiss_index(embeddings)

print("FAISS index created.")

# 6. Embed the user's question
query = "What types of income are taxable under income from other sources?"

query_embedding = model.encode(query)

# 7. Search FAISS
distances, indices = search_faiss(
    index,
    query_embedding,
    k=3
)

# 8. Display results
print("\nTop results:\n")

for distance, index_number in zip(distances, indices):
    chunk = chunks[index_number]

    print(f"Distance: {distance:.4f}")
    print(f"Page: {chunk['page']}")
    print(chunk["text"][:500])
    print("-" * 60)