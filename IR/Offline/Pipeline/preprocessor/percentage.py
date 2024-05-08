import re
from num2words import num2words

def replace_percentages(sentence):
    tokens = sentence.split()
    for i, token in enumerate(tokens):
        if '%' in token:
            numeric_part = re.search(r'(\d+(?:\.\d+)?)', token)
            if numeric_part:
                numeric_value = numeric_part.group(1)
                replaced_percent = num2words(float(numeric_value), lang='en').replace(' ', '') + "percent"
                tokens[i] = replaced_percent
    return ' '.join(tokens)


# sentence = "The text has  7% "
# sentence = replace_percentages(sentence)
# print(sentence)