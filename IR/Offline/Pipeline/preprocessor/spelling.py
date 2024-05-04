from Pipeline.preprocessor import spell


def correct_sentence_spelling(sentences):
    corrected_sentences = []
    for token in sentences:
        corrected_sentences.append(spell(token))
    return corrected_sentences
