import re


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

print(chunk_text(text))
