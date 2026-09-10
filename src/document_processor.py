import pymupdf

def extract_text_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document):
        text = page.get_text()

        pages.append({
            "text": text,
            "page": page_number + 1
        })

    document.close()

    return pages

def create_chunks(pages, chunk_size=1000, overlap=200):
    chunks = []

    for page in pages:
        text = page["text"].strip()

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "page": page["page"]
            })

            start += chunk_size - overlap

    return chunks