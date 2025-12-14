import os
from typing import List

# Optional libraries for supported formats
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None

# ----------------------------
# Loader functions for formats
# ----------------------------
def load_txt(file_path: str) -> str:
    """Load plain text file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(file_path: str) -> str:
    """Load PDF file"""
    if PdfReader is None:
        raise ImportError("PyPDF2 library is not installed")
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_docx(file_path: str) -> str:
    """Load DOCX file"""
    if Document is None:
        raise ImportError("python-docx library is not installed")
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Map file extensions to loader functions
SUPPORTED_LOADERS = {
    ".txt": load_txt,
    ".pdf": load_pdf,
    ".docx": load_docx
}

# ----------------------------
# Generic loader function
# ----------------------------
def load_file(folder_path: str = "data") -> List[str]:
    """
    Load all supported files from a folder and return a list of texts.
    """
    data = []
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return data

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue

        suffix = os.path.splitext(file_name)[1].lower()
        if suffix in SUPPORTED_LOADERS:
            try:
                data.append(SUPPORTED_LOADERS[suffix](file_path))
            except Exception as e:
                print(f"Error loading {file_name}: {e}")
        else:
            print(f"Unsupported file type: {suffix}")
    return data
