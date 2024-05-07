from toolz import pipe
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.numtowords import convert_num2words
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling1, correct_sentence_spelling2
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, to_sentences


def preprocessor(text):
    return pipe(text,
                lower,
                to_sentences,  # processes that require sentence tokens
                correct_sentence_spelling1,
                ' '.join,
                to_tokens,  # processes that require word tokens
                correct_sentence_spelling2,
                convert_num2words,
                remove_punctuation,
                remove_stopwords,
                stem,
                remove_empty_tokens,
                ' '.join
                )


print(preprocessor(r'''1-9-1990'''))