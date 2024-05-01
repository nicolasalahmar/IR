from Pipeline.preprocessor import spell


def correct_sentence_spelling(tokens):
    corrected_tokens = []
    for token in tokens:
        corrected_tokens.append(spell(token))
    return corrected_tokens
