import numerizer

from Offline.Pipeline.preprocessor import nlp


def replace_number(text, entity, offset):
    beg, end = entity.start_char, entity.end_char
    try:
        replacement = numerizer.numerize(entity.text)
    except ZeroDivisionError:
        replacement = entity.text
    except Exception:
        replacement = entity.text
    res = text[:beg + offset] + replacement + text[end + offset:]
    og_len = len(entity.text)
    new_len = len(replacement)
    offset = (new_len - og_len) + offset

    return res, offset


def numerize_text(text):
    nlp_text = nlp(text)
    entities = nlp_text.ents

    offset = 0
    for entity in entities:
        print(entity.label_, entity.text)
        if entity.label_ == 'CARDINAL':
            text, offset = replace_number(text, entity, offset)

    return text


if __name__ == "__main__":
    s = 'ten'
    print(numerize_text(s))
