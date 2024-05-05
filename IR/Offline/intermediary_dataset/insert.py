from alive_progress import alive_bar
from Helper.ORM import bulk_insert_records
import sqlite3
from toolz import pipe
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling1, correct_sentence_spelling2
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_sentences, to_tokens
from Pipeline.preprocessor.num2words import convert_num2words


def preprocessor(text):
    return pipe(text,
                to_sentences,
                correct_sentence_spelling1,
                ' '.join,
                to_tokens,
                correct_sentence_spelling2,
                convert_num2words,
                remove_punctuation,
                remove_stopwords,
                remove_empty_tokens,
                ' '.join
                )


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
