from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet


def stemmer(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]


def tokenize(text):
    return word_tokenize(text)


def pos_tagging(tokens):
    return pos_tag(tokens)


def get_wordnet_pos(tag_parameter):
    tag = tag_parameter[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def lemmatization(tokens):
    pos_tags = pos_tag(tokens)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]
