from nltk import word_tokenize, sent_tokenize


def to_tokens(text):
    return word_tokenize(text)


def to_sentences(text):
    return sent_tokenize(text)
