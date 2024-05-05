from atpbar import atpbar
from Helper.ORM import bulk_insert_records
import sqlite3
from toolz import pipe
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling1
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_sentences, to_tokens
from Pipeline.preprocessor.num2words import convert_num2words


def preprocessor(text):
    return pipe(text,
                lower,
                to_sentences,
                correct_sentence_spelling1,
                ' '.join,
                to_tokens,
                # correct_sentence_spelling2,
                convert_num2words,
                remove_punctuation,
                remove_stopwords,
                remove_empty_tokens,
                ' '.join
                )


def insert_records(name, records):
    for i in atpbar(range(len(records)), name=name):
        records[i].text = preprocessor(records[i].text)
    bulk_insert_records('intermediary_dataset/partially_processed_dataset1.db', records)


def create_table():
    sqliteConnection = sqlite3.connect('intermediary_dataset/partially_processed_dataset1.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS corpus (id TEXT PRIMARY KEY, TEXT TEXT);')
    sqliteConnection.commit()


def split_arr(records1, n):
    chunk_size = int(len(records1) / n)
    return [records1[i:i + chunk_size] for i in range(0, len(records1), chunk_size)]
