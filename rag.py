import re


text = """
Machine learning is a field of artificial intelligence.
It allows computers to learn patterns from data.
Supervised learning uses labeled data for training.
Unsupervised learning works with unlabeled data.
Deep learning uses neural networks with multiple layers.
These networks are trained using algorithms such as gradient descent.
"""

def chunk_text(text, chunk_size=100, overlap=0):
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "

        else:
            chunks.append(current_chunk.strip())

            overlap_text = current_chunk[-overlap:] if overlap > 0 else ""
            current_chunk = overlap_text + " " + sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
print(chunk_text(text))
