import re
from datetime import datetime

from num2words import num2words

date_pattern = r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})"


def extract_date(match, token):
    month, day, year = match
    month_name = datetime(year=int(year), month=int(month), day=1).strftime('%B').lower()
    written_date = f"{month_name} {num2words(int(day), lang='en')}, {num2words(int(year), lang='en')}"
    return re.sub(date_pattern, written_date, token, count=1).replace(' ', '')


def convert_date_format(tokens):
    for i, token in enumerate(tokens):
        matches = re.findall(date_pattern, token)
        for match in matches:
            try:
                tokens[i] = extract_date(match, token)
            except ValueError:
                try:
                    match = (match[1], match[0], match[2])
                    tokens[i] = extract_date(match, token)
                except Exception:
                    pass

    return tokens


if __name__ == '__main__':
    tokens = ["19-2-2022", "1-1-2024", "3-12-2025"]
    converted_tokens = convert_date_format(tokens)
    print(converted_tokens)
