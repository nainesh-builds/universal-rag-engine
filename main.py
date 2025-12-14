# from ingestion.file_loader import load_file, load_txt_folder, load_text_file
# from preprocessing.chunker import chunk_text

# if __name__ == "__main__":
#     # Path to your sample file (txt, PDF, or DOCX later)
#     file_path = "data/sample.txt"

#     # # Load the file content
#     # text = load_file(file_path)
#     # # Split the text into chunks
#     # chunks = chunk_text(text)

#     folder_path = "data"  # Folder containing multiple .txt files
#     text = load_txt_folder(folder_path)
#     chunks = chunk_text(text)

#     # Print results
#     print(f"Total chunks: {len(chunks)}")
#     # print("\nFirst chunk:\n")
#     # print(chunks[1:])

#     for i, chunk in enumerate(chunks[:9]):
#         print(f"---Chunk {i+1} ---\n{chunks}\n")

# main.py
from ingestion.file_loader import load_file
from preprocessing.chunker import chunk_text
from embeddings.embedding_generator import EmbeddingGenerator
from vectorstore.faiss_store import FAISSStore

# 1️⃣ Load all files from the folder
text = load_file("data")

# 2️⃣ Chunk the text
chunks = chunk_text(text, chunk_size=500, overlap=50)
print(f"Total chunks created: {len(chunks)}")

# 3️⃣ Generate embeddings
embedder = EmbeddingGenerator()
embeddings = embedder.generate(chunks)
print(f"Embeddings shape: {embeddings.shape}")

# 4️⃣ Store embeddings in FAISS and save
store = FAISSStore(embedding_dim=embeddings.shape[1])
store.add(embeddings, chunks)
store.save("faiss_index")
print("FAISS index saved successfully!")
