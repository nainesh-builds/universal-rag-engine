# app.py
import os
import streamlit as st
import faiss
import numpy as np
import pickle
from embeddings.embedding_generator import EmbeddingGenerator

st.title("Document Q&A - RAG Prototype")

# Paths for FAISS index and chunks
faiss_path = "faiss_index_index.faiss"
chunks_path = "faiss_index_chunks.pkl"

# Check if FAISS files exist
if not os.path.exists(faiss_path) or not os.path.exists(chunks_path):
    st.error("FAISS index not found. Please run main.py first to generate it.")
else:
    # Load FAISS index and chunks
    faiss_index = faiss.read_index(faiss_path)
    with open(chunks_path, "rb") as f:
        text_chunks = pickle.load(f)

    embedder = EmbeddingGenerator()

    # User input
    query = st.text_input("Ask a question:")

    if query:
        query_emb = embedder.generate([query])
        D, I = faiss_index.search(np.array(query_emb).astype("float32"), k=3)

        st.write("### Top relevant chunks:")
        for i in I[0]:
            if i < len(text_chunks):
                st.write("-", text_chunks[i])
