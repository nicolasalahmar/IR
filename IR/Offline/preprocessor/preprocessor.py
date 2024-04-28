from nltk.corpus import stopwords
from autocorrect import Speller
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string


def remove_punctuation(tokens):
    translator = str.maketrans('', '', string.punctuation)
    tokens_punctuated = [token.translate(translator) for token in tokens]
    return tokens_punctuated


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens


spell = Speller(lang='en')


def correct_sentence_spelling(tokens):
    corrected_tokens = []
    for token in tokens:
        corrected_tokens.append(spell(token))
    return corrected_tokens


def stem(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return stemmed_tokens


def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens


def preprocessor(text):
    tokens = word_tokenize(text)

    unpunctuated_tokens = remove_punctuation(tokens)
    no_stop_words_tokens = remove_stopwords(unpunctuated_tokens)
    spell_checked_tokens = correct_sentence_spelling(no_stop_words_tokens)
    stemmed_tokens = stem(spell_checked_tokens)
    lemmatized_tokens = lemmatize(stemmed_tokens)
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text
