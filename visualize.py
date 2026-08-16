from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


sentences = [
    "Python is commonly used for machine learning.",
    "Python is a popular language for AI development.",
    "Neural networks learn patterns from data.",
    "Gradient descent optimizes neural network parameters.",
    "I like eating pizza.",
    "The car is parked outside."
]


model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(sentences)

print("Original shape:", embeddings.shape)


pca = PCA(n_components=2)

reduced = pca.fit_transform(embeddings)

print("Reduced shape:", reduced.shape)


plt.figure(figsize=(10, 6))

for i, sentence in enumerate(sentences):
    x, y = reduced[i]

    plt.scatter(x, y)
    plt.annotate(sentence[:25], (x, y))

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Sentence Embeddings")

plt.show()