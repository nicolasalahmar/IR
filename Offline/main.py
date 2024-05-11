import os
from Helper.ORM import fetch_records
from Helper.timing import Timing
from Pipeline.index.index import Index
from dotenv import load_dotenv

load_dotenv()


def create_index_and_save():
    # fetching new records
    records = fetch_records(os.getenv('dataset'))
    documents = [rec.text for rec in records]
    index = Index(records)
    index.save()
    return index, documents


def initialize_query(text):
    preprocessed_query = preprocessor(text)
    return index.vectorizer.transform([preprocessed_query])


def find_similarities(query_vector):
    # find the similarity between the two vectors (query vector and vectors in the index)
    cosine_similarities = cosine_similarity(query_vector, index.tfidf_matrix)
    # make the two-dimensional matrix of similarities a one-dimensional list of scores
    cosine_similarities = cosine_similarities.flatten()
    # sort the similarities based on the highest score of similarity
    sorted_indices = np.argsort(cosine_similarities)[::-1]

    return sorted_indices, cosine_similarities


def print_similar_docs(sorted_indices, cosine_similarities, documents):
    # for i, idx in enumerate(sorted_indices):
    #     print(f"Document {idx}: Similarity Score {cosine_similarities[idx]}")
    #     print(documents[idx])
    top_n = 10
    top_documents = [(idx, cosine_similarities[idx]) for idx in sorted_indices[:top_n]]
    for idx, score in top_documents:
        print(f"Document {idx}: Similarity Score {score}")


if __name__ == '__main__':
    with Timing('Creating Index...'):
        # index, documents = create_index_and_save()
        index = Index.load(model_name=os.getenv("saved_model_name"), tfidf_name=os.getenv("saved_tfidf_name"), keys_name=os.getenv("saved_keys_name"))

    # preprocess the query create the query vector
    query_vector = initialize_query('1775')

    sorted_indices, cosine_similarities = find_similarities(query_vector)

    print_similar_docs(sorted_indices, cosine_similarities, documents)



