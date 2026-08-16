import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity



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


# 1. Create chunks
chunks = chunk_text(text)

print("DOCUMENT CHUNKS")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)


# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 3. Create embeddings for our chunks
chunk_embeddings = model.encode(chunks)


# 4. User query
query = "How do neural networks learn?"

query_embedding = model.encode([query])


# 5. Compare query with every chunk
scores = cosine_similarity(
    query_embedding,
    chunk_embeddings
)[0]


# 6. Rank chunks by similarity
results = sorted(
    zip(scores, chunks),
    reverse=True
)


# 7. Display results
print("\nSEARCH RESULTS")

for score, chunk in results:
    print(f"\nScore: {score:.4f}")
    print(chunk)