from country_named_entity_recognition import find_countries


def handle_sentence(text):
    abbreviations = {
        "u.s.a.": "unitedstates",
        "u.s.a":"unitedstates",
    }


    for abbrev, full_form in abbreviations.items():
        text = text.replace(abbrev, full_form)

    countries = find_countries(text,True)

    replacements = {country[1].group(): country[0].name for country in countries}

    for country_name, original_name in replacements.items():
        original_name = original_name.replace(" ", "").lower()
        text = text.replace(country_name, original_name)

    return text


def replace_countries(sentences):
    corrected_sentences = []
    for sentence in sentences:
        corrected_sentences.append(handle_sentence(sentence))
    return corrected_sentences

#
# sentences =["u.s.a","u.s.a."]
# new_text = replace_countries(sentences)
# print(new_text)
