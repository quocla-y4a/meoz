# import openai
# from config import openai_api_key
# from meoz.vector_store import query_similar_documents

# openai.api_key = openai_api_key

# def build_prompt(question):
#     relevant_chunks = query_similar_documents(question)
#     context = "\n\n".join(relevant_chunks)
#     return f"""
# Bạn là Meoz - trợ lý BI thân thiện.
# Hãy trả lời câu hỏi dựa trên thông tin sau:

# --- Kiến thức nội bộ ---
# {context}

# --- Câu hỏi ---
# {question}
# """

# def ask(question):
#     prompt = build_prompt(question)
#     res = openai.ChatCompletion.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "Bạn là Meoz - trợ lý thân thiện từ phòng BI."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return res["choices"][0]["message"]["content"].strip()


from openai import OpenAI
from config import openai_api_key
from bot_config.vector_store import query_similar_documents

client = OpenAI(api_key=openai_api_key)

def build_prompt(question):
    relevant_chunks = query_similar_documents(question)
    context = "\n\n".join(relevant_chunks)
    return f"""
Bạn là Meoz - trợ lý BI thân thiện.
Hãy trả lời câu hỏi dựa trên thông tin sau:

--- Kiến thức nội bộ ---
{context}

--- Câu hỏi ---
{question}
"""

def ask(question):
    prompt = build_prompt(question)
    print("\n===== PROMPT GỬI GPT =====\n")
    print(prompt[:1500])
    print("==========================\n")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Meoz - BI Assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

