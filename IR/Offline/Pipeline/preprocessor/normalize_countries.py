from country_named_entity_recognition import find_countries

from Offline.Pipeline.preprocessor import nlp


def replace_cner(sample):
    country = find_countries(sample, True)
    if country:
        new_name = country[0][0].name.replace(' ', '')
        matched = country[0][1].group()
        sample = sample.replace(matched, new_name)
        return sample
    else:
        return sample



def replace_Spacy(text, entity, offset):
    beg, end = entity.start_char, entity.end_char

    substring = text[beg + offset:end + offset]
    new_text = replace_cner(substring)

    res = text[:beg + offset] + new_text + text[end + offset:]
    og_len = len(entity.text)
    new_len = len(new_text)
    offset = (new_len - og_len) + offset
    return res, offset


def replace_countries(text):
    nlp_text = nlp(text)
    entities = nlp_text.ents
    offset = 0
    for entity in entities:
        if entity.label_ == 'GPE':
            text, offset = replace_Spacy(text, entity, offset)

    return text
