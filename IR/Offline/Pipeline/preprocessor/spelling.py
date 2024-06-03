from Offline.Pipeline.preprocessor import spell
from typing import List
from spellchecker import SpellChecker


def correct_sentence_spelling1(sentences):
    corrected_sentences = []
    for token in sentences:
        corrected_sentences.append(spell(token))
    return corrected_sentences


def correct_sentence_spelling2(tokens: List[str]) -> List[str]:
    spell = SpellChecker()
    misspelled = spell.unknown(tokens)
    for i, token in enumerate(tokens):
        if token in misspelled:
            corrected = spell.correction(token)
            if corrected is not None:
                tokens[i] = corrected
    return tokens
