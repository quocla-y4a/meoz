# import sys
# from bot_config.loader import load_documents
# # from bot_config.vector_store import add_documents, query_similar_documents, reset_collection
# from bot_config.vector_store import add_documents, query_similar_documents, reset_collection
# from bot_config.qa import ask
# import os

# def index():
#     folder_path = os.path.join(os.path.dirname(__file__), "knowledge_base")
#     print(f"📅 Đang đọc dữ liệu từ thư mục: {folder_path}")
#     docs = load_documents(folder_path)
#     add_documents(docs)
#     print(f"✅ Meoz đã đọc {len(docs)} đoạn từ tài liệu.")

# def chat(question):
#     print(f"\n❓ Câu hỏi: {question}")
#     answer = ask(question)
#     print(f"\n🧠 Meoz trả lời:\n{answer}")

# def reset():
#     reset_collection()
#     print("✅ Collection đã được xoá.")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Dùng: python main.py [index|ask|reset] [câu hỏi neu có]")
#         sys.exit(1)

#     command = sys.argv[1]

#     if command == "index":
#         index()
#     elif command == "ask":
#         if len(sys.argv) < 3:
#             print("Vui lòng nhập câu hỏi sau 'ask'")
#         else:
#             chat(" ".join(sys.argv[2:]))
#     elif command == "reset":
#         reset()
#     else:
#         print(f"Lệnh không hợp lệnh: {command}")

import sys
import os
from bot_config.loader import load_documents
from bot_config.vector_store import add_documents
from bot_config.qa import ask

def index():
    folder_path = os.path.join(os.path.dirname(__file__), "knowledge_base")
    print(f"📁 Đang đọc dữ liệu từ thư mục: {folder_path}")
    docs = load_documents(folder_path)
    add_documents(docs)
    print(f"✅ Meoz đã đọc {len(docs)} đoạn từ tài liệu.")

def chat(question):
    print(f"\n❓ Câu hỏi: {question}")
    answer = ask(question)
    print(f"\n🧠 Meoz trả lời:\n{answer}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Dùng: python main.py [index|ask] [câu hỏi nếu có]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "index":
        index()
    elif command == "ask":
        if len(sys.argv) < 3:
            print("Vui lòng nhập câu hỏi sau 'ask'")
        else:
            chat(" ".join(sys.argv[2:]))
    else:
        print(f"Lệnh không hợp lệ: {command}")