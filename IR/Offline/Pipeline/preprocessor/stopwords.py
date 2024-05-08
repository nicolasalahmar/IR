from Pipeline.preprocessor import stop_words


def remove_stopwords(text):
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

