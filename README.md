# AI Tax Document Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that answers questions about the Indian Income-tax Act, 2025 using official tax-document content.

The application retrieves relevant passages from the tax document, provides the retrieved context to a Gemini language model, and displays source/page citations with the answer.

## Architecture

```text
Income-tax Act, 2025 PDF
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
Sentence Transformer Embeddings
        ↓
FAISS Vector Index
        ↓
User Question
        ↓
Question Embedding
        ↓
Semantic Retrieval
        ↓
Retrieved Tax Document Context
        ↓
Gemini LLM
        ↓
Grounded Answer + Source Citations
        ↓
Streamlit UI

## Tech Stack

Python
Streamlit
PyMuPDF
Sentence Transformers
FAISS
Google Gemini API
python-dotenv

## How It Works
### 1. Document Processing

The application extracts text from the Income-tax Act, 2025 PDF using PyMuPDF.

The extracted text is divided into overlapping chunks while preserving page metadata.

### 2. Embeddings

Each text chunk is converted into a numerical vector using:

sentence-transformers/all-MiniLM-L6-v2

The model produces 384-dimensional embeddings.

### 3. Semantic Retrieval

FAISS stores the document embeddings and performs similarity search when a user asks a question.

The application retrieves the most relevant chunks from the tax document.

### 4. Retrieval-Augmented Generation

The retrieved chunks are added to a prompt and sent to Gemini.

The model is instructed to answer using only the retrieved document context and not to invent unsupported information.

### 5. Source Citations

The model identifies supporting sources using references such as [Source 1].

Python then maps those source references back to the retrieved chunks and displays the corresponding document page.

This keeps page metadata controlled by the application rather than asking the LLM to generate page numbers.

### Grounding

If the retrieved documents do not contain enough information to answer a question, the application responds:

I could not find this information in the provided tax documents.

This helps prevent the model from answering questions using unsupported general knowledge.

## Running Locally
# 1. Clone the repository
git clone https://github.com/brindaJ9/ai-tax-document-assistant.git
cd ai-tax-document-assistant
# 2. Create and activate a virtual environment
python -m venv .venv

Windows PowerShell:

.venv\Scripts\Activate.ps1
# 3. Install dependencies
pip install -r requirements.txt
# 4. Add your Gemini API key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Never commit the .env file to GitHub.

# 5. Run the application
streamlit run app.py

The application will open in your browser.

## Project Structure
ai-tax-document-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── tax documents
│
├── src/
│   ├── citations.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── prompt.py
│   ├── rag.py
│   ├── retriever.py
│   └── vector_store.py
│
└── tests/
    ├── test_citations.py
    ├── test_embeddings.py
    ├── test_extraction.py
    ├── test_llm.py
    ├── test_prompt.py
    ├── test_rag.py
    ├── test_retrieval.py
    └── test_retriever.py

# Current Scope

The current version focuses on answering questions grounded in the Income-tax Act, 2025.

Additional tax documents are retained in the project dataset for potential future expansion of the retrieval pipeline.

# Limitations
The application depends on the quality of the retrieved document chunks.
Complex questions may require better query formulation or retrieval strategies.
The system is not a substitute for professional tax advice.
The current version uses a local FAISS index built when the application starts.