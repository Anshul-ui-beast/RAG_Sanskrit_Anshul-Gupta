import os
import requests
import pandas as pd
import joblib

# 1. Configuration
DOC_FOLDER = "documents"
EMBEDDING_MODEL = "bge-m3"  # Great for Multilingual/Sanskrit
OLLAMA_API = "http://localhost:11434/api/embed"

def create_embedding(text_list):
    """Generates embeddings using local CPU via Ollama"""
    response = requests.post(OLLAMA_API, json={
        "model": EMBEDDING_MODEL,
        "input": text_list
    })
    return response.json().get("embeddings", [])

# 2. Load and Chunk Data
chunks_data = []
chunk_id = 0

print("📂 Reading documents...")
files = [f for f in os.listdir(DOC_FOLDER) if f.endswith('.txt')]

for file in files:
    with open(os.path.join(DOC_FOLDER, file), "r", encoding="utf-8") as f:
        text = f.read()
    
    # Simple chunking by double newlines (paragraphs)
    # For better results, you could use a RecursiveCharacterTextSplitter
    raw_chunks = text.split("\n\n")
    
    # Filter empty chunks
    raw_chunks = [c.strip() for c in raw_chunks if c.strip()]
    
    for content in raw_chunks:
        chunks_data.append({
            "chunk_id": chunk_id,
            "source": file,
            "text": content
        })
        chunk_id += 1

print(f"🧩 Created {len(chunks_data)} text chunks.")

# 3. Vectorization (Embeddings)
print("🧠 Generating Embeddings (Running on CPU)...")
texts = [c["text"] for c in chunks_data]
embeddings = create_embedding(texts)

# Attach embeddings to data
for i, chunk in enumerate(chunks_data):
    chunk["embedding"] = embeddings[i]

# 4. Save Index
df = pd.DataFrame(chunks_data)
joblib.dump(df, "sanskrit_embeddings.joblib")
print("✅ Indexing complete! Saved to 'sanskrit_embeddings.joblib'")