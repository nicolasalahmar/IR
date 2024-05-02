from num2words import num2words
from decimal import Decimal

def is_num(word):
    return word.isdigit()


def convert_num2words(tokens):
    for idx, token in enumerate(tokens):
        if is_num(token):
            tokens[idx] = num2words(Decimal(str(token)), lang='en').replace(' ', '')
    return tokens
