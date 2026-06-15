import os
import faiss
from sentence_transformers import SentenceTransformer

# Load documents and chunks
folder = "documents"
all_chunks = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        chunks = text.split("\n\n")
        all_chunks.extend(chunks)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(all_chunks)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Ask question
query = input("Ask a question: ")

query_embedding = model.encode([query])

# Search top 3 results
D, I = index.search(query_embedding, k=3)

print("\nQuestion:", query)
print("\nTop Matches:\n")

for idx in I[0]:
    print(all_chunks[idx])
    print("-" * 50)