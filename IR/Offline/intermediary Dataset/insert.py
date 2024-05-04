import sys

from Helper.ORM import bulk_insert_records
from Pipeline.preprocessor.num2words import convert_num2words
from nltk import word_tokenize
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling
from Pipeline.preprocessor.stopwords import remove_stopwords
import sqlite3

from Pipeline.preprocessor.tokenize import to_sentences


def preprocessor(text):
    sentneces = to_sentences(text)
    spell_checked_docs = correct_sentence_spelling(sentneces)
    spell_checked_docs = ' '.join(spell_checked_docs)

    tokens = word_tokenize(spell_checked_docs)
    num_handled_tokens = convert_num2words(tokens)
    unpunctuated_tokens = remove_punctuation(num_handled_tokens)
    no_stop_words_tokens = remove_stopwords(unpunctuated_tokens)
    no_empty_strings = list(filter(None, no_stop_words_tokens))
    processed_text = ' '.join(no_empty_strings)
    return processed_text


def insert_records(records):
    for record in records:
        record.text = preprocessor(record.text)
    bulk_insert_records('partially_processed_dataset1.db', records)


def create_table():
    sqliteConnection = sqlite3.connect('partially_processed_dataset1.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS corpus (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()
