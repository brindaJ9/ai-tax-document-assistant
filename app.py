import streamlit as st

from src.rag import build_rag_pipeline, answer_question
from src.citations import get_cited_sources


st.set_page_config(
    page_title="AI Tax Document Assistant",
    page_icon="📄"
)


st.title("📄 AI Tax Document Assistant")

st.write(
    "Ask questions about the Indian Income-tax Act, 2025 "
    "using the provided tax documents."
)


@st.cache_resource
def load_rag_pipeline():
    pdf_path = "data/income_tax_act_2025.pdf"

    return build_rag_pipeline(pdf_path)


model, index, chunks = load_rag_pipeline()


question = st.text_input(
    "Ask a question",
    placeholder="e.g. What income is chargeable under income from other sources?"
)


if st.button("Ask"):
    if question.strip():

        with st.spinner("Searching the tax document and generating an answer..."):

            answer, retrieved_chunks = answer_question(
                question,
                model,
                index,
                chunks,
                k=3
            )

        st.subheader("Answer")

        st.write(answer)

        sources = get_cited_sources(
            answer,
            retrieved_chunks
        )

        if sources:
            st.subheader("Sources")

            for source in sources:
                st.write(
                    f"• Source {source['source_number']} — "
                    f"Income-tax Act, 2025 — Page {source['page']}"
                )

    else:
        st.warning("Please enter a question.")