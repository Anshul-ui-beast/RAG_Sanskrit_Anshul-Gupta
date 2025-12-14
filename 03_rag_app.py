import pandas as pd
import numpy as np
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity

# --- Configuration ---
EMBEDDING_MODEL = "bge-m3"
LLM_MODEL = "llama3.2" # Lightweight 3B model optimized for CPU
OLLAMA_GENERATE = "http://localhost:11434/api/generate"
OLLAMA_EMBED = "http://localhost:11434/api/embed"

def get_embedding(text):
    r = requests.post(OLLAMA_EMBED, json={"model": EMBEDDING_MODEL, "input": [text]})
    return r.json()["embeddings"][0]

def llm_inference(prompt):
    print("\n🤖 Generating answer (CPU)...")
    r = requests.post(OLLAMA_GENERATE, json={
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    })
    return r.json()["response"]

# 1. Load Knowledge Base
print("📂 Loading Knowledge Base...")
try:
    df = joblib.load("sanskrit_embeddings.joblib")
except FileNotFoundError:
    print("❌ Error: 'sanskrit_embeddings.joblib' not found. Run ingest.py first.")
    exit()

# 2. User Interface
while True:
    print("\n" + "="*50)
    query = input("❓ Ask a question (Sanskrit/English) [or 'exit']: ")
    if query.lower() == 'exit': break

    # 3. Retrieve
    query_vec = get_embedding(query)
    
    # Calculate Similarity
    # Stack all embeddings into a matrix
    matrix = np.vstack(df["embedding"].values)
    similarities = cosine_similarity(matrix, [query_vec]).flatten()
    
    # Get Top 3 relevant chunks
    top_indices = similarities.argsort()[::-1][0:3]
    top_chunks = df.iloc[top_indices]
    
    # Format Context
    context_text = "\n---\n".join(top_chunks["text"].tolist())
    
    # 4. Generate Prompt
    # We instruct the LLM to act as a Sanskrit scholar helper
    prompt = f"""
    You are a helpful assistant proficient in Sanskrit and English. 
    Use the following retrieved context chunks from Sanskrit stories to answer the user's question.
    
    Context:
    {context_text}
    
    User Question: "{query}"
    
    Answer clearly based ONLY on the context provided. If the answer is not in the context, say so.
    """
    
    # 5. Output
    answer = llm_inference(prompt)
    print("\n💡 Answer:")
    print(answer)