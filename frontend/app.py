import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Intelligent Document Assistant",
    page_icon="📄",
    layout="wide"
)

with st.sidebar:
    st.markdown("Document Assistant")
    st.markdown("Free RAG-based AI (No API key)")
    st.divider()

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:
        with st.spinner("Indexing document..."):
            response = requests.post(
                f"{BACKEND_URL}/upload/",
                files={"file": uploaded_file}
            )

        if response.status_code == 200:
            st.success("Document indexed")
        else:
            st.error("Upload failed")

    st.divider()
    st.markdown("### 🛠 Tech Stack")
    st.markdown("""
    - Streamlit  
    - FastAPI  
    - FAISS  
    - GPT4All  
    - HuggingFace  
    """)

st.markdown(
    """
    <h1 style='text-align:center;'>🤖 Intelligent Document Assistant</h1>
    <p style='text-align:center;color:gray;font-size:18px;'>
    Chat with your PDF using a FREE local AI model
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input(
    "💬 Ask a question",
    placeholder="What is this document about?"
)

col1, col2, _ = st.columns([1, 1, 4])

with col1:
    ask = st.button("🚀 Ask")

with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.session_state.chat = []

if ask and query:
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{BACKEND_URL}/ask/",
            json={"question": query}
        )

    if res.status_code == 200:
        answer = res.json()["answer"]
        st.session_state.chat.append(
            {"q": query, "a": answer}
        )
    else:
        st.error("Backend error")

for item in reversed(st.session_state.chat):
    st.markdown(
        f"""
        <div style="background:#f1f3f6;padding:15px;border-radius:10px;">
        <b>🧑 You:</b><br>{item['q']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="background:#e8f0fe;padding:15px;border-radius:10px;margin-top:5px;">
        <b>🤖 Assistant:</b><br>{item['a']}
        </div><br>
        """,
        unsafe_allow_html=True
    )

st.divider()
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ | Free RAG AI</p>",
    unsafe_allow_html=True
)
