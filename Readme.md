# Sanskrit Document RAG (CPU-Optimized)

A Retrieval-Augmented Generation (RAG) system designed to process Sanskrit narratives and answer user queries using purely CPU-based inference. This project utilizes **Ollama** for local LLM and embedding generation, ensuring data privacy and offline capability.

## 📖 Overview

This system ingests a corpus of Sanskrit stories (such as *The Foolish Servant* and *Clever Kalidasa*), creates a vector index, and allows users to chat with the content in English or Sanskrit. It is optimized to run efficiently on standard hardware without requiring a GPU.

## ✨ Features

* **Sanskrit Support:** optimized for processing Devanagari script and Sanskrit morphology using the `bge-m3` embedding model.
* **CPU Inference:** Fully local execution using quantized models via Ollama.
* **Semantic Search:** Retrieves context based on meaning rather than just keyword matching.
* **Cross-Lingual QA:** Supports querying in English about Sanskrit content and vice-versa.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

1.  **Python 3.8+**
2.  **Ollama**: [Download here](https://ollama.com/)
3.  **AI Models**: You need to pull the specific models used in the pipeline. Open your terminal and run:
    ```
    ollama pull bge-m3
    ollama pull llama3.2
    ```

## 📦 Installation

1.  **Clone the repository** (or create a folder for your project).
2.  **Install Python dependencies**:
    ```
    pip install pandas requests scikit-learn joblib numpy
    ```

## 🚀 Usage Guide

Follow these steps strictly in order to set up and run the system.

### Step 1: Start the Inference Server
Ensure Ollama is running in the background to handle API requests.
```bash
ollama serve
```
Step 2: Data Preparation
Run the data creation script to generate the raw text file from the source stories (e.g., Mūrkhabhṛtyasya, Chaturasya Kālidāsasya).


```

python 01_create_data.py

```
Output: Creates a documents/sanskrit_stories.txt file.

Step 3: Ingestion & Indexing
Run the ingestion script to read the text, chunk it, generate embeddings, and save the vector index.

Bash

python 02_ingest.py
Output: Generates sanskrit_embeddings.joblib (The Vector Database).

Step 4: Run the Chat Application
Start the RAG interface to ask questions about the stories.

Bash

python 03_rag_app.py
Example Interaction
Plaintext

❓ Ask a question: Who is Shankhanada?
🤖 Generating answer (CPU)...
💡 Answer: Shankhanada is the servant of Govardhanadasa. In the story, he is depicted as foolish...
📂 Project Structure
Plaintext

.
├── 01_create_data.py      # Extracts raw Sanskrit text from source
├── 02_ingest.py           # Chunking and Vector Embedding pipeline
├── 03_rag_app.py          # RAG Inference and Chat Interface
├── documents/             # Folder containing raw text files
│   └── sanskrit_stories.txt
├── sanskrit_embeddings.joblib # The serialized Vector Store
└── README.md              # Project documentation
🧩 Technical Details
Embeddings: BAAI/bge-m3 (1024 dimensions) - chosen for superior multilingual performance.

LLM: Llama-3.2-3B - chosen for low latency on CPU while maintaining reasoning capabilities.

Retrieval: Cosine Similarity via Scikit-Learn.


Data Source: Includes stories like The Foolish Servant , Clever Kalidasa , The Old Woman's Cleverness , The Devotee , and The Cold Hurts.