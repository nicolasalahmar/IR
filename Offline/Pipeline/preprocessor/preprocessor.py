from toolz import pipe

from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.normalize_countries import replace_countries
from Pipeline.preprocessor.numerize import numerize_text
from Pipeline.preprocessor.ordinal_nums import replace_ordinal_numbers
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, whitespace_tokenize, to_sentences


def preprocessor(text):
    return pipe(text,
                lower,

                whitespace_tokenize,
                remove_stopwords,
                ' '.join,


                to_sentences,
                replace_countries,
                ' '.join,


                to_sentences,
                numerize_text,
                ' '.join,

                to_tokens,
                stem,
                replace_ordinal_numbers,
                remove_punctuation,
                remove_empty_tokens,
                ' '.join,

                )


if __name__ == '__main__':
    print(preprocessor(r'''It is the (secant(x))^2; or you could write it as (cos(x))^(-2) or 1/(cos(x))^2.. . But basically the secant squared is the most elegant answer.'''))

