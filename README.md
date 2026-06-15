# Private-GTP-for-Company
PrivateGPT is a local AI-powered document question-answering system using FAISS, Sentence Transformers, and Llama 3 via Ollama. It enables semantic search and intelligent responses from custom documents through a Flask web interface.
PrivateGPT – AI Document Q&A System

PrivateGPT is a Retrieval-Augmented Generation (RAG) based AI system that allows users to ask natural language questions from their private documents and receive intelligent answers.

The system uses FAISS for fast semantic search and Llama 3 (via Ollama) to generate human-like responses based on retrieved context.

🚀 Features
📄 Document-based question answering
🔍 Semantic search using FAISS
🧠 AI-generated responses using Llama 3 (Ollama)
⚡ Fast embedding search with Sentence Transformers
🌐 Flask-based web interface
🔒 Fully local execution (no API required)
🧠 Tech Stack
Python
Flask
FAISS (Vector Database)
Sentence Transformers
Ollama (Llama 3)
HTML, CSS

⚙️ How It Works
Documents are loaded and split into chunks
Each chunk is converted into embeddings
FAISS stores embeddings for similarity search
User query is converted into embeddings
Most relevant chunks are retrieved
Llama 3 generates final answer using context

📌 Use Cases
Company internal knowledge assistant
HR policy chatbot
Document Q&A system
Personal AI assistant for files

<img width="959" height="442" alt="Screenshot 2026-06-16 001406" src="https://github.com/user-attachments/assets/916b2617-5dec-4b46-82da-a5bd22071ced" />


<img width="950" height="424" alt="image" src="https://github.com/user-attachments/assets/3fcc1d63-a56b-4ce9-ac84-3bc1c974fd6e" />
