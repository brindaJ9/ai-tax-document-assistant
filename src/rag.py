from src.retriever import build_retriever, retrieve
from src.prompt import create_rag_prompt
from src.llm import ask_llm


def build_rag_pipeline(pdf_path):
    model, index, chunks = build_retriever(pdf_path)

    return model, index, chunks


def answer_question(question, model, index, chunks, k=3):
    # 1. Retrieve relevant chunks
    retrieved_chunks = retrieve(
        question,
        model,
        index,
        chunks,
        k=k
    )

    # 2. Build the RAG prompt
    prompt = create_rag_prompt(
        question,
        retrieved_chunks
    )

    # 3. Send the prompt to Gemini
    answer = ask_llm(prompt)

    return answer, retrieved_chunks