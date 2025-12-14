import faiss
import numpy as np
import pickle

class FAISSStore:
    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.text_chunks = []

    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings).astype("float32"))
        self.text_chunks.extend(chunks)

    def search(self, query_emb, top_k=3):
        D, I = self.index.search(np.array(query_emb).astype("float32"), top_k)
        return [self.text_chunks[i] for i in I[0] if i < len(self.text_chunks)]

    def save(self, path):
        faiss.write_index(self.index, f"{path}_index.faiss")
        with open(f"{path}_chunks.pkl", "wb") as f:
            pickle.dump(self.text_chunks, f)

    @classmethod
    def load(cls, path):
        dummy = cls(embedding_dim=1)  # placeholder, will overwrite
        dummy.index = faiss.read_index(f"{path}_index.faiss")
        with open(f"{path}_chunks.pkl", "rb") as f:
            dummy.text_chunks = pickle.load(f)
        dummy.embedding_dim = dummy.index.d
        return dummy
