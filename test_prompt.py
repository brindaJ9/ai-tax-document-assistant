from src.prompt import create_rag_prompt


retrieved_chunks = [
    {
        "page": 159,
        "text": "Income of every kind which is not to be excluded from the total income under this Act, shall be chargeable to income-tax under the head 'Income from other sources'."
    }
]


question = "What income is chargeable under income from other sources?"


prompt = create_rag_prompt(
    question,
    retrieved_chunks
)


print(prompt)