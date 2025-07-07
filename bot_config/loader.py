import os
import pdfplumber
from unstructured.partition.auto import partition


def split_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    print(f"📚 Tổng số đoạn sinh ra: {len(chunks)}")
    return chunks

def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if not filename.lower().endswith(".pdf"):
            continue
        text = load_text_from_file(path)
        chunks = split_text(text)
        for i, chunk in enumerate(chunks):
            docs.append({
                "id": f"{filename}_{i}",
                "content": chunk,
                "metadata": {"source": filename}
            })
    return docs

def load_text_from_file(filepath):
    if filepath.lower().endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join([page.extract_text() or "" for page in pdf.pages])
        print(f"📄 {os.path.basename(filepath)} - Tổng ký tự: {len(text)}")
        return text
    else:
        return ""
