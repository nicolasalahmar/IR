from alive_progress import alive_bar
from Helper.ORM import bulk_insert_records
from nltk import word_tokenize
import sqlite3
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_sentences
from Pipeline.preprocessor.num2words import convert_num2words


def preprocessor(text):
    sentences = to_sentences(text)
    spell_checked_docs = correct_sentence_spelling(sentences)
    spell_checked_docs = ' '.join(spell_checked_docs)

    tokens = word_tokenize(spell_checked_docs)
    num_handled_tokens = convert_num2words(tokens)
    unpunctuated_tokens = remove_punctuation(num_handled_tokens)
    no_stop_words_tokens = remove_stopwords(unpunctuated_tokens)
    no_empty_strings = list(filter(None, no_stop_words_tokens))
    processed_text = ' '.join(no_empty_strings)
    return processed_text


def insert_records(records):
    l = len(records)
    with alive_bar(l) as bar:
        for record in records:
            record.text = preprocessor(record.text)
            bar()
    bulk_insert_records('intermediary_dataset/partially_processed_dataset1.db', records)


def create_table():
    sqliteConnection = sqlite3.connect('intermediary_dataset/partially_processed_dataset1.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS corpus (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()
