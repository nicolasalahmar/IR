from Offline.Pipeline.preprocessor import nlp


def NER(text):
    doc = nlp(text)
    return text, doc.ents
