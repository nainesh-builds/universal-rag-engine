# ingestion/file_loader.py
import os

# List supported file types (expandable later)
SUPPORTED_EXTENSIONS = [".txt",".pdf", ".docx"]  # later add ".pdf", ".docx"

def load_file(folder_path):
    """
    Reads all supported files in the given folder and returns concatenated text.
    Skips unsupported files automatically.
    """
    all_text = ""

    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        if not os.path.isfile(fpath):
            continue  # skip subfolders
        suffix = os.path.splitext(fname)[1].lower()
        if suffix in SUPPORTED_EXTENSIONS:
            with open(fpath, "r", encoding="utf-8") as f:
                all_text += f.read() + "\n"
        else:
            print(f"Skipping unsupported file type: {fname}")

    if not all_text:
        raise ValueError("No supported files found in the folder.")
    
    return all_text
