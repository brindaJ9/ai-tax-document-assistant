from src.citations import format_sources


retrieved_chunks = [
    {
        "page": 159,
        "text": "Income of every kind..."
    },
    {
        "page": 465,
        "text": "Taxable regular income..."
    },
    {
        "page": 41,
        "text": "Some other text..."
    }
]


sources = format_sources(retrieved_chunks)


print("Sources:\n")

for source in sources:
    print(f"• {source}")