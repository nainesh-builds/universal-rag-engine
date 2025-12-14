# chunk_size=500 - each chunk is 500 characters long
# overlap=50 - next chunk starts 50 characters before the previous chunk ended

def chunk_text(text: str, chunk_size=1000, overlap=50):
    """
    Split text into chunks of chunk_size with overlap
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
    