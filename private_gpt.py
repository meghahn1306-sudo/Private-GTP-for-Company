import os
import faiss
from sentence_transformers import SentenceTransformer
from ollama import chat

print("Loading documents...")

folder = "documents"
all_chunks = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        chunks = text.split("\n\n")
        all_chunks.extend(chunks)

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(all_chunks)

print("Creating FAISS index...")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("PrivateGPT Ready!")

while True:
    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])

    D, I = index.search(query_embedding, k=3)

    context = "\n".join([all_chunks[idx] for idx in I[0]])

    prompt = f"""
You are a company assistant.

Answer ONLY from the provided context.
Do not make assumptions.
Do not perform calculations unless explicitly mentioned.
If the answer is not present in the context, say:
'I could not find that information in the documents.'

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

    print("\nAnswer:")
    print(response["message"]["content"])