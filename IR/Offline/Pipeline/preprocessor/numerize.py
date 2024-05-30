import numerizer

from Offline.Pipeline.preprocessor import nlp


def numerize_text(sentences):
    corrected_sentences = []
    for sentence in sentences:
        try:
            doc = nlp(sentence)
            numerized_sentence = numerizer.numerize(doc.text)
            corrected_sentences.append(numerized_sentence)
        except ZeroDivisionError:
            corrected_sentences.append(sentence)
    return corrected_sentences
