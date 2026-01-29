<<<<<<< HEAD
Gen AI Document Assistant

1. Overview:

This project is an AI-powered document assistant using Retrieval-Augmented Generation technology. It reads PDF documents, processes their content into vector embeddings, and answers user queries intelligently using large language models.
The system has a backend built with FastAPI and a frontend using Streamlit. It supports embedding models, vector stores, and LLMs to provide accurate and fast responses.

2. Features:

Upload PDF files for processing
Convert PDF content into chunks and embeddings
Store embeddings in a vector store using FAISS
Ask questions about the uploaded documents
Generate answers using GPT4All LLM
Frontend interface for easy interaction

3. Tech Stack:

Backend Python FastAPI LangChain Community LangChain Classic
Frontend Streamlit
Vector Store FAISS
Embeddings HuggingFace Sentence Transformers
LLM GPT4All
PDF Loader PyPDFLoader

4. Installation:

Clone the repository
git clone <your-repo-url>
cd <repository-folder>

Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate on Windows

Install dependencies
pip install -r requirements.txt

Place your GPT4All model in the path specified in rag_pipeline.py
C:/Users/<username>/AppData/Local/nomic.ai/GPT4All/Phi-3-mini-4k-instruct-Q4_0.gguf

5. Usage:

Run Backend:
uvicorn main:app --reload
Open Swagger UI at http://127.0.0.1:8000/docs
Upload PDF files using the /upload/ endpoint
Ask questions using the /ask/ endpoint
Run Frontend:
streamlit run app.py
Open the browser at the URL displayed in Streamlit terminal
Interact with your document assistant

6. Notes:

Make sure the uploaded PDF is not too large to avoid long processing times
GPT4All currently works on CPU. Using GPU with supported models can speed up embedding processing
Ensure all required paths for model files and vector stores are correct

7. Future Enhancements:

Support multiple PDF uploads at once
Add GPU acceleration for embeddings and LLM inference
Store vector stores persistently to avoid reprocessing
=======
# RAG-Document-Assistant-Project
RAG Document Assistant – A Retrieval-Augmented Generation system to answer user queries from PDF documents using LLMs, FAISS vector databases, and Hugging Face models.
>>>>>>> e6c26f7d22ebdee0b33a34489c834b474044549f
