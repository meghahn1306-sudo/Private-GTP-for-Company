from flask import Flask, render_template, request
import os
import faiss
from sentence_transformers import SentenceTransformer
from ollama import chat

app = Flask(__name__)

# Load documents
folder = "documents"
all_chunks = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        chunks = text.split("\n\n")
        all_chunks.extend(chunks)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(all_chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        query = request.form["query"]

        query_embedding = model.encode([query])

        D, I = index.search(query_embedding, k=3)

        context = "\n".join([all_chunks[idx] for idx in I[0]])

        prompt = f"""
You are a company assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{query}
"""

        response = chat(
            model="llama3.2:1b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response["message"]["content"]

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)