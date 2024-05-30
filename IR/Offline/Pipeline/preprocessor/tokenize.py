from nltk import word_tokenize, sent_tokenize
from Pipeline.preprocessor.find_email import find_email
from Pipeline.preprocessor.find_url import find_url
from nltk.tokenize import WhitespaceTokenizer


def to_tokens(text):
    emails, text_with_email_placeholder = find_email(text)
    urls, text_with_url_placeholder = find_url(text_with_email_placeholder)
    tokens = word_tokenize(text_with_url_placeholder)

    for i, token in enumerate(tokens):
        if token == 'EMAIL_ADDRESS':
            tokens[i] = emails.pop(0)
        if token == 'URL' and urls:
            tokens[i] = urls.pop(0)

    return tokens


def to_sentences(text):
    return sent_tokenize(text)


def whitespace_tokenize(text):
    return WhitespaceTokenizer().tokenize(text)
