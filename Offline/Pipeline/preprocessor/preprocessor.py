from toolz import pipe

from Pipeline.preprocessor.NER import NER
from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.html import clean_html
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.normalize_countries import replace_countries
from Pipeline.preprocessor.normalize_dates import replace_dates
from Pipeline.preprocessor.normalize_organizations import replace_organisations
from Pipeline.preprocessor.numerize import numerize_text
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.remove_long_words import remove_long_words
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, whitespace_tokenize, to_sentences


def preprocessor(text):
    return pipe(text,

                #clean_html,

                replace_countries,
                # replace_dates,
                # number normalization (modify numerize)


                # lower,

                # whitespace_tokenize,
                # remove_stopwords,
                # ' '.join,

                # to_tokens,
                # ordinal numbers normalization
                # remove_punctuation,
                # remove_long_words,
                # stem,
                # remove_empty_tokens,
                # ' '.join,
                )


if __name__ == '__main__':
    #print(preprocessor(r'''<!-- START YAHOO ANSWERS BADGE -->. <!-- make sure to cut and paste all the badge code -->. <style>. /* . This is the style information that you may edit to change how the badge appears on your web page.. You can change the appearance of just about everything if you'd really like to.  . For more information about CSS, visit http://www.w3schools.com/css/css_intro.asp. Quick Tip: To hide something, just add "display: none;" inside its style definition, without the quotes.  . */. . #ya-badge { border: 1px #54c40b solid; background-color: #fff; width: 163px; padding:0px; font-family:arial; }. #ya-badge #ya-faces { background:url("http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/badge_emoticon.gif"); width: 163px; height:53px; }. #ya-badge a { color:#3499cc!important; text-decoration:none; }. #ya-badge a:hover { color:#006699; text-decoration:underline; }. #ya-badge #ya-badge-content #ya-badge-title { display:block;font-family: arial; font-weight:bold; font-size: 13px; margin-top:5px; margin-left:10px; margin-bottom:5px;}. #ya-badge #ya-badge-content ul { padding:0px!important;margin:0px!important;list-style-type: none!important;padding-left: 0px!important; border:0px!important; background-color: #fff;}. #ya-badge #ya-badge-content ul .ya-listitem { margin-left:10px!important; margin-right:10px!important; list-style-type: none!important; padding: 0px!important; font-family: arial; margin-bottom:3px; padding-bottom:3px; border-bottom:1px #dfdfdf solid; text-indent: 0px!important;}. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-title { font-size: 11px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata {display:block; color: #333; font-size: 9px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata a {color: #333!important; font-size: 9px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata a:hover { color:#006699; text-decoration:underline; }. #ya-badge #ya-more-link { font-size: 10px; text-align:right; display:block; margin:5px; } . #ya-badge #ya-badge-content #ya-level-area { color: #787878; display:block; background:url('http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/pointsstar.gif'); background-repeat:no-repeat; background-position:10px 4px; padding:3px; padding-left:30px; font-size:12px; background-color: #fcfbe7;  }. #ya-badge #ya-badge-content #ya-level-area a { color: #787878!important; }. #ya-badge #ya-badge-content #ya-level-area .ya-level-number { font-weight:bold;  }. #ya-badge #visit-link { margin:5px; margin-left:10px; color:#8b8b8c; font-size:10px; margin-top:5px; }. #ya-badge #visit-link a { color:#8b8b8c!important; text-decoration:underline; }. </style>. . <div id="ya-badge">. <div id="ya-logo"><a href="http://answers.yahoo.com/"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/ga_ans_badge.gif"></a></div>. <div id="ya-faces"><a href="http://answers.yahoo.com/question/?link=ask"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a><a href="http://answers.yahoo.com/dir/?link=ask&more=y"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a><a href="http://answers.yahoo.com/dir/?link=over&more=y"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a></div>. . <div id="ya-badge-content">. . <!-- . This is the code that gets the latest information from the Yahoo! Answers servers.  Don't change this unless you really know what you're doing.  . There are some options you may edit at your own risk:. - size:'''))

    #Test ORG
    # print(preprocessor("apple is looking at buying U.K. startup for $1 billion. I love eating Apple"))

    #Test Date
    print(preprocessor("in january 1948 ballen acquired the interest of goode and became the sole owner he then moved the company to philadelphia pennsylvania where the label was based for the rest of its existence until 1956 the label specialized in rhythm and blues ivin ballen died in miami beach florida in february 1978 gotham s most notable contribution to american music was the release of recordings by the acoustic bluesman dan pickett originally recorded in 1949 another artist who recorded for gotham included doug quattlebaum his song lizzie lou was one of the last releases for the label doris browne was a singer who around the 1949 1950 period had she performed on a weekly show which was broadcast by wpen am in philadelphia the hour long show was called the parisian tailor kiddie hour in 1953 the label appeared to be keen to push browne s profile with her single please believe me bw oh baby she was backed by doc bagby on that recording he also backed her on her single until the end of time bw why don t you love me now now now gotham g 296 and another recording the game of love bw my cherie"))