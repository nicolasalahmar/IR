import importlib
import os

from dotenv import load_dotenv
from peewee import *

load_dotenv()

# default database
db = SqliteDatabase(os.getenv('dataset'))


class Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Corpus._meta.database = db

    class Meta:
        database = db


class Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Countries_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Countries_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Countries_Numerize_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Countries_Numerize_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Countries_Numerize_Stem_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Countries_Numerize_Stem_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Countries_Numerize_Stem_Ordinal_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Countries_Numerize_Stem_Ordinal_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_Countries_Numerize_Stem_Ordinal_Punc_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_Countries_Numerize_Stem_Ordinal_Punc_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_countries_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_countries_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class countries_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        countries_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class countries_dates_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        countries_dates_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class org_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        org_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Numerize_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Numerize_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Numerize_punct_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Numerize_punct_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Numerize_punct_ord_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Numerize_punct_ord_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Numerize_punct_ord_long_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Numerize_punct_ord_long_Processed_Corpus._meta.database = db

    class Meta:
        database = db


class Lower_Stopwords_HTML_Countries_Numerize_punct_ord_long_stem_Processed_Corpus(Model):
    id = CharField(primary_key=True)
    text = CharField(unique=True)

    @staticmethod
    def set_db(db):
        Lower_Stopwords_HTML_Countries_Numerize_punct_ord_long_stem_Processed_Corpus._meta.database = db

    class Meta:
        database = db


def class_for_name(class_name, module_name='Offline.Helper.model'):
    try:
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    except AttributeError:
        return None
