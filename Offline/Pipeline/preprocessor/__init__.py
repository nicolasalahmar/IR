from autocorrect import Speller
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from spacy import load

spell = Speller(lang='en')

nlp = load('en_core_web_sm')

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()
