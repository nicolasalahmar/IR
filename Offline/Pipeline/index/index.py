import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from Pipeline.matching_ranking.match import find_similarities, get_top_docs
from Pipeline.preprocessor.tokenize import to_tokens
from Pipeline.preprocessor.preprocessor import preprocessor


class Index:
    def __init__(self, corpus=None):
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        if corpus is not None:
            self.documents, self.keys = self.DocsKeys()
            self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        else:
            pass

    def DocsKeys(self):
        documents = [record.text for record in self.corpus]
        keys = [record.id for record in self.corpus]
        return documents, keys

    def create_dataframe(self):
        return pd.DataFrame(self.tfidf_matrix.toarray(), columns=self.vectorizer.get_feature_names_out(),
                            index=self.keys)

    def save(self, model_name="Pipeline/index/Saved/model.pickle", tfidf_name="Pipeline/index/Saved/tfidf.pickle", keys_name="Pipeline/index/Saved/keys.pickle"):
        pickle.dump(self.vectorizer, open(model_name.replace('.pickle', str(len(self.keys)) + '.pickle'), 'wb'))
        pickle.dump(self.tfidf_matrix, open(tfidf_name.replace('.pickle', str(len(self.keys)) + '.pickle'), "wb"))
        pickle.dump(self.keys, open(keys_name.replace('.pickle', str(len(self.keys)) + '.pickle'), "wb"))

    @staticmethod
    def load(model_name="Pipeline/index/Saved/model.pickle", tfidf_name="Pipeline/index/Saved/tfidf.pickle", keys_name="Pipeline/index/Saved/keys.pickle"):
        i = Index()
        i.tfidf_matrix = pickle.load(open(tfidf_name, 'rb'))
        i.vectorizer = pickle.load(open(model_name, 'rb'))
        i.keys = pickle.load(open(keys_name, 'rb'))
        return i

    def search(self, query):
        # preprocess the query create the query vector
        query_vector = self.initialize_query(query)
        sorted_indices, cosine_similarities = find_similarities(query_vector, self)
        return get_top_docs(sorted_indices, cosine_similarities, self.keys)

    def initialize_query(self, text):
        preprocessed_query = preprocessor(text)
        return self.vectorizer.transform([preprocessed_query])
