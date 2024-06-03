import string


def remove_punctuation(tokens):
    translator = str.maketrans('', '', string.punctuation)
    tokens_punctuated = [token.translate(translator) for token in tokens]
    return tokens_punctuated
