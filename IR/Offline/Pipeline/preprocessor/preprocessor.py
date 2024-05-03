from Pipeline.preprocessor.num2words import convert_num2words
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens


def preprocessor(text):
    tokens = to_tokens(text)
    num_handled_tokens = convert_num2words(tokens)
    unpunctuated_tokens = remove_punctuation(num_handled_tokens)
    no_stop_words_tokens = remove_stopwords(unpunctuated_tokens)
    spell_checked_tokens = correct_sentence_spelling(no_stop_words_tokens)
    stemmed_tokens = stem(spell_checked_tokens)
    processed_text = ' '.join(stemmed_tokens)

    return processed_text
