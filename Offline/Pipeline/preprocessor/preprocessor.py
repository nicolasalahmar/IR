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
from Pipeline.preprocessor.tokenize import to_tokens, to_sentences, whitespace_tokenize


def preprocessor(text):
    return pipe(text,
                lower,

                to_sentences,
                correct_sentence_spelling1,
                ' '.join,

                whitespace_tokenize,
                remove_stopwords,
                ' '.join,

                to_tokens,
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
    print(preprocessor(r'''It is the (secant(x))^2; or you could write it as (cos(x))^(-2) or 1/(cos(x))^2.. . But basically the secant squared is the most elegant answer.'''))

