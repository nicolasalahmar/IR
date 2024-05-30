from Offline.Pipeline.preprocessor import stop_words


def remove_stopwords(tokens):
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens