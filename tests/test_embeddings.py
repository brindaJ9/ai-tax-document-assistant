from src.embeddings import load_embedding_model


model = load_embedding_model()

text = "Income from dividends may be taxable."

embedding = model.encode(text)

print("Embedding type:", type(embedding))
print("Embedding shape:", embedding.shape)
print("First 10 values:", embedding[:10])
