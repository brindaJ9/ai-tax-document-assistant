from src.document_processor import extract_text_from_pdf, create_chunks
from src.embeddings import load_embedding_model
from src.vector_store import create_faiss_index, search_faiss


def build_retriever(pdf_path):
    # 1. Extract text from PDF
    pages = extract_text_from_pdf(pdf_path)

    # 2. Create chunks
    chunks = create_chunks(pages)

    # 3. Load embedding model
    model = load_embedding_model()

    # 4. Create embeddings for all chunks
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)

    # 5. Create FAISS index
    index = create_faiss_index(embeddings)

    return model, index, chunks


def retrieve(query, model, index, chunks, k=3):
    # Convert the question into an embedding
    query_embedding = model.encode(query)

    # Search for the most relevant chunks
    distances, indices = search_faiss(
        index,
        query_embedding,
        k=k
    )

    results = []

    for distance, index_number in zip(distances, indices):
        chunk = chunks[index_number]

        results.append({
            "text": chunk["text"],
            "page": chunk["page"],
            "distance": float(distance)
        })

    return results