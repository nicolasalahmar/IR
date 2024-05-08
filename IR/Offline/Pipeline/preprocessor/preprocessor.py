from toolz import pipe

from Pipeline.preprocessor.date_to_text import convert_date_format
from Pipeline.preprocessor.replace_dates import replace_dates
from Pipeline.preprocessor.ordinal_nums import replace_ordinal_numbers
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.numtowords import convert_num2words
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.spelling import correct_sentence_spelling1
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, to_sentences


def preprocessor(text):
    return pipe(text,
                lower,
                to_sentences,  # processes that require sentence tokens
                correct_sentence_spelling1,
                ' '.join,
                remove_stopwords,
                to_tokens,  # processes that require word tokens
                stem,
                convert_date_format,
                replace_dates,
                replace_ordinal_numbers,
                convert_num2words,
                remove_punctuation,
                remove_empty_tokens,
                ' '.join
                )


if __name__ == '__main__':
    print(preprocessor('nicolasalahmar@gmail.com'))
