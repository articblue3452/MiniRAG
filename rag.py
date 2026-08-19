import re

import faiss
from sentence_transformers import SentenceTransformer


text = """
Machine learning is a field of artificial intelligence.
It allows computers to learn patterns from data.
Supervised learning uses labeled data for training.
Unsupervised learning works with unlabeled data.
Deep learning uses neural networks with multiple layers.
These networks are trained using algorithms such as gradient descent.
"""


def chunk_text(text, chunk_size=150, overlap_sentences=1):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current = []

    for sentence in sentences:
        current_text = " ".join(current)

        if len(current_text) + len(sentence) <= chunk_size:
            current.append(sentence)
        else:
            chunks.append(" ".join(current))

            current = current[-overlap_sentences:]
            current.append(sentence)

    if current:
        chunks.append(" ".join(current))

    return chunks


# Create chunks
chunks = chunk_text(text)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(chunks)

# Normalize for cosine similarity
faiss.normalize_L2(embeddings)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

# Add document embeddings
index.add(embeddings)


def search(query, k=3):
    query_embedding = model.encode([query])

    # Normalize query for cosine similarity
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, k)

    results = []

    for score, index_number in zip(scores[0], indices[0]):
        results.append({
            "score": float(score),
            "text": chunks[index_number]
        })

    return results


query = input("Ask something: ")

results = search(query)

print("\nSearch results:")

for result in results:
    print(f"\nScore: {result['score']:.4f}")
    print(result["text"])