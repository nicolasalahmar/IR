from Pipeline.preprocessor.num2words import convert_num2words
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, to_sentences


def preprocessor(text):
    # processes that require sentence tokens
    sentences = to_sentences(text)
    spell_checked_docs = correct_sentence_spelling(sentences)
    spell_checked_docs = ' '.join(spell_checked_docs)

    # processes that require word tokens
    tokens = to_tokens(spell_checked_docs)
    num_handled_tokens = convert_num2words(tokens)
    unpunctuated_tokens = remove_punctuation(num_handled_tokens)
    no_stop_words_tokens = remove_stopwords(unpunctuated_tokens)
    stemmed_tokens = stem(no_stop_words_tokens)
    no_empty_strings = list(filter(None, stemmed_tokens))
    processed_text = ' '.join(no_empty_strings)

    return processed_text
