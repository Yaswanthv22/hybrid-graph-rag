import streamlit as st


st.set_page_config(
    page_title="Hybrid Graph RAG",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Hybrid Graph RAG")

st.write(
    "Upload a PDF document and ask questions using "
    "Vector + Knowledge Graph retrieval."
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    question = st.text_input(
        "Ask a question about the document"
    )

    if question:
        st.write("Question:", question)
