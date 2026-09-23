from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = [
    "I enjoy coding.",
    "I like programming.",
    "The weather is very hot."
]

embeddings = model.encode(sentences)

for i, sentence in enumerate(sentences):
    print("\nSentence:", sentence)
    print("Embedding:", embeddings[i])
    print("Embedding dimensions:", len(embeddings[i]))

similarity = cosine_similarity([embeddings[0]], [embeddings[1]])

print("\nSimilarity between:")
print(sentences[0])
print("and")
print(sentences[1])
print("Similarity score:", similarity[0][0])