import os

folder = "documents"

print("Files found:", os.listdir(folder))

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        print(f"\n----- {filename} -----")
        print(file.read()[:200])