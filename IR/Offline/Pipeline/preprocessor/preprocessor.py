from toolz import pipe

from Pipeline.preprocessor.date_to_text import convert_date_format
from Pipeline.preprocessor.replace_dates import replace_dates
from Pipeline.preprocessor.ordinal_nums import replace_ordinal_numbers
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
                remove_stopwords,
                stem,
                convert_date_format,
                replace_dates,
                replace_ordinal_numbers,
                convert_num2words,
                remove_punctuation,
                remove_empty_tokens,
                ' '.join
                )

# print(preprocessor(r'''1/1/1990 5th 4th century bce second book c 2nd 1st century bce is the first of the twelve angas part of the agamas religious texts which were compiled based on the teachings of mahavira the existing text of the acharanga sutra which is used by the svetambara sect of jainism was recompiled and edited by kshamashraman devardhigani who headed the council held at valabhi c 454 ce the digambaras do not recognize the available text and regard the original text as having been lost in its original form the digambara text mulachara is said to be derived from the original acharanga and discusses the conduct of a digambara monk the acharanga sutra is the oldest agam from a linguistic point of view written in ardhamagadhi prakrit the sutra contains two books or srutaskandhas the first book is the older part to which other treatises were later added it describes the conduct and behavior of ascetic life the mode of asking for food bowl clothes conduct while walking and speaking and regulation of possessions by ascetics it also describes the penance of mahavira the great hero the second book is divided into four sections called kulas there were originally five k l'''))