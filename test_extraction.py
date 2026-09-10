from src.document_processor import extract_text_from_pdf, create_chunks


pdf_path = "data/income_from_other_sources.pdf"

pages = extract_text_from_pdf(pdf_path)

print(f"Number of pages: {len(pages)}")

chunks = create_chunks(pages)

print(f"Number of chunks: {len(chunks)}")

print("\n--- First chunk ---\n")
print(chunks[0]["text"])

print("\nPage:", chunks[0]["page"])