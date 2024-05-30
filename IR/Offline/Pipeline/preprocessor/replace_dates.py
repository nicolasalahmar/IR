import re
from num2words import num2words


def replace_dates(tokens):
    for i, token in enumerate(tokens):
        match_decades = re.match(r'(\d{4})s', token)
        if match_decades:
            decade = match_decades.group(1)
            replaced_decade = num2words(int(decade), lang='en').replace(' ', '')
            tokens[i] = replaced_decade
    return tokens


if __name__ == '__main__':
    tokens = ["1990s", "2110s", "15th", "hello"]
    print(replace_dates(tokens))
