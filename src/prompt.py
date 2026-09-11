def create_rag_prompt(question, retrieved_chunks):
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"[Source {i} | Page {chunk['page']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an AI assistant that answers questions about the Indian Income-tax Act, 2025.

Use ONLY the information provided in the sources below to answer the user's question.

If the answer cannot be found in the provided sources, say:
"I could not find this information in the provided tax documents."

Do not rely on your general knowledge.
Do not invent facts, sections, rates, deductions, or interpretations.

When making a factual statement, cite the relevant source using its source number,
for example [Source 1].

Sources:
--------------------
{context}
--------------------

User question:
{question}

Answer clearly and concisely.
"""

    return prompt