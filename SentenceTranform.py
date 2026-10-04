from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

q1 = input("Question 1: ")
q2 = input("Question 2: ")

embeddings = model.encode([q1, q2])

score = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

similarity = score[0][0]

print(f"\nSimilarity Score: {similarity:.2f}")

if similarity > 0.8:
    print("Duplicate Questions")
else:
    print("Different Questions")