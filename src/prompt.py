def create_rag_prompt(question, retrieved_chunks):
    context = "\n\n".join(
        f"Page {chunk['page']}:\n{chunk['text']}"
        for chunk in retrieved_chunks
    )

    prompt = f"""
You are an AI assistant that answers questions about the Indian Income-tax Act, 2025.

Use ONLY the information provided in the context below to answer the user's question.

If the answer cannot be found in the provided context, say:
"I could not find this information in the provided tax documents."

Do not rely on your general knowledge.
Do not invent facts, sections, rates, deductions, or interpretations.

Context:
--------------------
{context}
--------------------

User question:
{question}

Answer clearly and concisely.
"""

    return prompt