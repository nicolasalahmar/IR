from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from preprocessor.preprocessor import preprocessor


def create_index(corpus):
    vectorizer = TfidfVectorizer(preprocessor=preprocessor)
    documents = [record[1] for record in corpus]
    keys = [record[0] for record in corpus]
    tfidf_matrix = vectorizer.fit_transform(documents)
    return pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=keys)
