import re


def format_sources(retrieved_chunks):
    sources = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        sources.append({
            "source_number": i,
            "page": chunk["page"]
        })

    return sources


def get_cited_sources(answer, retrieved_chunks):
    cited_sources = []

    matches = re.findall(r"\[Source (\d+)\]", answer)

    for match in matches:
        source_number = int(match)

        if 1 <= source_number <= len(retrieved_chunks):
            chunk = retrieved_chunks[source_number - 1]

            source = {
                "source_number": source_number,
                "page": chunk["page"]
            }

            if source not in cited_sources:
                cited_sources.append(source)

    return cited_sources