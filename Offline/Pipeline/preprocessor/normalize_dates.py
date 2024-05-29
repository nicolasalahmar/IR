import datetime

from dateutil.parser import parse, ParserError

from Pipeline.preprocessor import nlp, default_date


def replace_DATE(text, entity, offset):
    beg, end = entity.start_char, entity.end_char
    try:
        dt = parse(str(entity.text), default=default_date)
        replacement = dt.strftime('%d%m%Y') + " " + dt.strftime('%Y') + " "+ dt.strftime('%B') + " " + dt.strftime('%B%d')
    except ParserError:
        replacement = entity.text
    res = text[:beg + offset] + replacement + text[end + offset:]
    og_len = len(entity.text)
    new_len = len(replacement)
    offset = (new_len - og_len) + offset

    return res, offset


def replace_dates(text):
    nlp_text = nlp(text)
    entities = nlp_text.ents

    offset = 0
    for entity in entities:
        if entity.label_ == 'DATE':
            text, offset = replace_DATE(text, entity, offset)

    return text


if __name__ == "__main__":
    s = 'in March ballen acquired the interest of goode and became'
    print(replace_dates(s))
