import re


text = """
Machine learning is a field of artificial intelligence.
It allows computers to learn patterns from data.
Supervised learning uses labeled data for training.
Unsupervised learning works with unlabeled data.
Deep learning uses neural networks with multiple layers.
These networks are trained using algorithms such as gradient descent.
"""


sentences = re.split(r'(?<=[.!?])\s+', text.strip())

print("Sentences:")
print(sentences)

for sentence in sentences:
    print(sentence)