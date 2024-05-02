from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from Helper.ORM import fetch_records
from Pipeline.index.index import Index
from datetime import datetime
from Pipeline.preprocessor.preprocessor import preprocessor

start = datetime.now()
records = fetch_records('dataset1.db', 100)
documents = [rec.text for rec in records]
index = Index(records)
index.save()
end = datetime.now()

print(index.create_dataframe())
print(end - start)

index = Index.load()
query = '1775'
preprocessed_query = preprocessor(query)
print(preprocessed_query)

query_vector = index.vectorizer.transform([preprocessed_query])

cosine_similarities = cosine_similarity(query_vector, index.tfidf_matrix)

cosine_similarities = cosine_similarities.flatten()

sorted_indices = np.argsort(cosine_similarities)[::-1]

for i, idx in enumerate(sorted_indices):
    print(f"Document {idx}: Similarity Score {cosine_similarities[idx]}")
    print(documents[idx])

top_n = 10
top_documents = [(idx, cosine_similarities[idx]) for idx in sorted_indices[:top_n]]
for idx, score in top_documents:
    print(f"Document {idx}: Similarity Score {score}")
