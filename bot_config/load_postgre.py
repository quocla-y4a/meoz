import psycopg2
from meoz.vector_store import add_documents

def load_data_from_postgres():
    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port=5432
    )

    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM project_data")

    rows = cursor.fetchall()
    docs = []

    for row in rows:
        doc_id, title, description = row
        content = f"Title: {title}\nDescription: {description}"
        docs.append({
            "id": f"pg_{doc_id}",
            "content": content,
            "metadata": {"source": "postgres"}
        })

    cursor.close()
    conn.close()

    add_documents(docs)
