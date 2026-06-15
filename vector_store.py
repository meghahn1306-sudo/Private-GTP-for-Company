import os
import faiss
from sentence_transformers import SentenceTransformer

folder = "documents"
all_chunks = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        chunks = text.split("\n\n")
        all_chunks.extend(chunks)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(all_chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Total Chunks:", len(all_chunks))
print("Vectors Stored:", index.ntotal)