# Sanskrit Document RAG (CPU-Optimized)

A **Retrieval-Augmented Generation (RAG)** system designed to process Sanskrit narratives and answer user queries using **purely CPU-based inference**.  
The project uses **Ollama** for local LLM and embedding generation, ensuring **data privacy, offline usage, and low-resource compatibility**.

---

## 📖 Overview

This system ingests a corpus of Sanskrit stories (such as *The Foolish Servant* and *Clever Kalidasa*), builds a vector index, and allows users to chat with the content in **Sanskrit or English**.

It is optimized to run efficiently on standard hardware **without requiring a GPU**.

---

## ✨ Key Features

- **Sanskrit Language Support**  
  Optimized for Devanagari script and Sanskrit morphology using the `bge-m3` embedding model.

- **CPU-Only Inference**  
  Fully local execution with quantized models via Ollama.

- **Semantic Search**  
  Retrieves context based on meaning rather than keyword matching.

- **Cross-Lingual Question Answering**  
  Ask questions in English about Sanskrit content and vice versa.

---

## 🛠️ Prerequisites

Make sure the following are installed:

- **Python 3.8+**
- **Ollama**  
  Download from: https://ollama.com/

### Required Models
Pull the models used in the pipeline:
```bash
ollama pull bge-m3
ollama pull llama3.2

📦 Installation

Clone the repository

git clone <your-repo-url>
cd <your-repo-name>


Install Python dependencies

pip install pandas requests scikit-learn joblib numpy

🚀 Usage Guide

Follow the steps in order.

Step 1: Start the Ollama Inference Server

Ensure Ollama is running in the background:

ollama serve

Step 2: Data Preparation

Generate the raw Sanskrit text from source stories
(e.g., Mūrkhabhṛtyasya, Chaturasya Kālidāsasya).

python 01_create_data.py


Output

documents/sanskrit_stories.txt

Step 3: Ingestion & Indexing

Chunk the text, generate embeddings, and store the vector index.

python 02_ingest.py


Output

sanskrit_embeddings.joblib

Step 4: Run the Chat Application

Start the RAG-based chat interface.

python 03_rag_app.py

Example Interaction
❓ Ask a question: Who is Shankhanada?
🤖 Generating answer (CPU)...
💡 Answer: Shankhanada is the servant of Govardhanadasa. In the story, he is depict as foolish...

📂 Project Structure
.
├── 01_create_data.py          # Extracts raw Sanskrit text from sources
├── 02_ingest.py               # Chunking & vector embedding pipeline
├── 03_rag_app.py              # RAG inference & chat interface
├── documents/
│   └── sanskrit_stories.txt   # Consolidated Sanskrit corpus
├── sanskrit_embeddings.joblib # Serialized vector store
└── README.md                  # Project documentation

🧩 Technical Details

Embeddings
BAAI/bge-m3 (1024 dimensions) – chosen for strong multilingual and Sanskrit support.

LLM
Llama-3.2-3B – optimized for low-latency CPU inference with solid reasoning ability.

Retrieval Method
Cosine similarity using Scikit-learn.

Data Sources
Includes stories such as:

The Foolish Servant

Clever Kalidasa

The Old Woman’s Cleverness

The Devotee

The Cold Hurts

✅ Highlights

Fully offline & private

No GPU required

Optimized for low-resource systems

Supports Sanskrit ↔ English interaction