import re
from num2words import num2words
from decimal import Decimal


def replace_ordinal_numbers(tokens):
    for i, token in enumerate(tokens):
        match = re.match(r'(\d+)(st|nd|rd|th)', token)
        if match:
            num, suffix = match.groups()
            num = int(num)
            replaced_num = num2words(Decimal(str(num)), lang='en',ordinal=True).replace(' ', '')
            tokens[i] = replaced_num
    return tokens


if __name__ == '__main__':
    tokens = ["1990s", "2110s", "15th", "1st", "2nd", "3rd", "421", "hello", '0.54']
    print(replace_ordinal_numbers(tokens))
