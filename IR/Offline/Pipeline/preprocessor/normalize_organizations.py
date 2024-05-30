import re

from Pipeline.preprocessor import nlp


def replace_ORG(text, entity, offset):
    beg, end = entity.start_char, entity.end_char
    replacement = entity.text.replace(' ', '_') + "_org"

    res = text[:beg + offset] + replacement + text[end + offset:]
    og_len = len(entity.text)
    new_len = len(replacement)
    offset = (new_len - og_len) + offset

    return res, offset


def replace_organisations(text):
    nlp_text = nlp(text)
    entities = nlp_text.ents
    offset = 0
    for entity in entities:
        if entity.label_ == 'ORG':
            text, offset = replace_ORG(text, entity, offset)

    return text
