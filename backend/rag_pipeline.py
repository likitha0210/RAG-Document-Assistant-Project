import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_community.llms import GPT4All

import state  #shared memory

VECTORSTORE_PATH = "vectorstore"

def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def build_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    state.vectorstore = FAISS.from_documents(docs, embeddings)
    state.vectorstore.save_local(VECTORSTORE_PATH)

    return state.vectorstore


def ask_question(question: str):
    if state.vectorstore is None:
        return "Please upload a PDF first."

    llm = GPT4All(
        model=r"C:\Users\kalya\AppData\Local\nomic.ai\GPT4All\Phi-3-mini-4k-instruct.Q4_0.gguf",
        backend="llama",
        verbose=True
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=state.vectorstore.as_retriever()
    )

    print("Invoking QA chain with question:", question)

    result = qa_chain.invoke({"query": question})
    return result["result"]
