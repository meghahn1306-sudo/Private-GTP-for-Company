import os

folder = "documents"
all_chunks = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

        chunks = text.split("\n\n")

        all_chunks.extend(chunks)

print("Total Chunks:", len(all_chunks))

for i, chunk in enumerate(all_chunks[:5]):
    print(f"\nChunk {i+1}:")
    print(chunk)