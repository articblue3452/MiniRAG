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

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is commonly used for machine learning.",
    "Python is a popular language for AI development.",
    "I like eating pizza.",
    "The car is parked outside."
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(embeddings)

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        print(
            f"\n{sentences[i]}"
            f"\nvs"
            f"\n{sentences[j]}"
            f"\nSimilarity: {similarity[i][j]:.4f}"
        )