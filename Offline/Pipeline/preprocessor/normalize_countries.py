from country_named_entity_recognition import find_countries

from Pipeline.preprocessor import nlp


def replace_GPE(text, entity, offset):
    country = find_countries(entity.text, True)
    beg, end = entity.start_char, entity.end_char
    if country:
        unified_country_name = country[0][0].name.replace(' ', '')
        res = text[:beg + offset] + unified_country_name + text[end + offset:]
        og_len = len(entity.text)
        new_len = len(unified_country_name)
        offset = (new_len - og_len) + offset
        return res, offset
    else:
        return text, offset


def replace_countries(text):
    nlp_text = nlp(text)
    entities = nlp_text.ents
    offset = 0
    for entity in entities:
        if entity.label_ == 'GPE':
            text, offset = replace_GPE(text, entity, offset)


    return text
