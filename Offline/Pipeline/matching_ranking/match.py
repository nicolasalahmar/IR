import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def find_similarities(query_vector, index):
    # find the similarity between the two vectors (query vector and vectors in the index)
    cosine_similarities = cosine_similarity(query_vector, index.tfidf_matrix)
    # make the two-dimensional matrix of similarities a one-dimensional list of scores
    cosine_similarities = cosine_similarities.flatten()
    # sort the similarities based on the highest score of similarity
    sorted_indices = np.argsort(cosine_similarities)[::-1]

    return sorted_indices, cosine_similarities


def get_top_docs(sorted_indices, cosine_similarities, keys, top_n=11):
    lst = []
    counter = 0
    for idx in sorted_indices[:top_n]:
        lst.append((keys[idx], cosine_similarities[idx], counter))
        counter += 1
    return lst
