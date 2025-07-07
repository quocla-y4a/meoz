import os
import chromadb
from openai import OpenAI
from config import openai_api_key

# Khởi tạo client cho Chroma (chuẩn mới nhất)
# chroma_client = chromadb.PersistentClient(path=os.path.join(os.path.dirname(__file__), "../.chroma_store"))
from chromadb.config import Settings

chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=None
))
# Định nghĩa collection
collection = chroma_client.get_or_create_collection(name="meoz_knowledge")

# Khởi tạo OpenAI client
client = OpenAI(api_key=openai_api_key)

def get_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

def add_documents(docs):
    print(f"📋 Tổng số đoạn sinh ra: {len(docs)}")
    for doc in docs:
        embedding = get_embedding(doc["content"])
        print(f"➕ Thêm đoạn ID: {doc['id']}, ký tự: {len(doc['content'])}")
        collection.add(
            documents=[doc["content"]],
            embeddings=[embedding],
            metadatas=[doc["metadata"]],
            ids=[doc["id"]]
        )

def query_similar_documents(question, n_results=5):
    embedding = get_embedding(question)
    results = collection.query(query_embeddings=[embedding], n_results=n_results)

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]

    if not docs:
        print("⚠️ No related documents found.")
    else:
        print(f"\n🌟 {len(docs)} đoạn được truy vấn:")
        for i, d in enumerate(docs):
            print(f"[{i+1}] {d[:150]}...")
            print(f"    📁 Source: {metas[i].get('source')}\n")

    return docs

def reset_collection():
    chroma_client.delete_collection(name="meoz_knowledge")
    print("🗑️ Đã xóa collection cũ.")
