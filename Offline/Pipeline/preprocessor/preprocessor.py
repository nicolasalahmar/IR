from toolz import pipe

from Pipeline.preprocessor.date_to_text import convert_date_format
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.lemmatizer import lemmatize
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.numerize import numerize_text
from Pipeline.preprocessor.numtowords import convert_num2words
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, whitespace_tokenize, to_sentences


def preprocessor(text):
    return pipe(text,
                lower,

                whitespace_tokenize,
                remove_stopwords,
                ' '.join,

                # to_sentences,
                # correct_sentence_spelling1,
                # ' '.join,

                to_sentences,
                numerize_text,
                ' '.join,

                # to_tokens,
                # lemmatize,
                # stem,
                # convert_date_format,
                # replace_dates,
                # replace_ordinal_numbers,
                # convert_num2words,
                # remove_punctuation,
                # remove_empty_tokens,
                # ' '.join
                )


if __name__ == '__main__':
    print(preprocessor(r'''It is the (secant(x))^2; or you could write it as (cos(x))^(-2) or 1/(cos(x))^2.. . But basically the secant squared is the most elegant answer.'''))

