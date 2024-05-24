from toolz import pipe

from Pipeline.preprocessor.empty_tokens import remove_empty_tokens
from Pipeline.preprocessor.html import clean_html
from Pipeline.preprocessor.lower import lower
from Pipeline.preprocessor.normalize_countries import replace_countries
from Pipeline.preprocessor.numerize import numerize_text
from Pipeline.preprocessor.ordinal_nums import replace_ordinal_numbers
from Pipeline.preprocessor.punctuation import remove_punctuation
from Pipeline.preprocessor.remove_long_words import remove_long_words
from Pipeline.preprocessor.stemmer import stem
from Pipeline.preprocessor.stopwords import remove_stopwords
from Pipeline.preprocessor.tokenize import to_tokens, whitespace_tokenize, to_sentences


def preprocessor(text):
    return pipe(text,
                lower,

                whitespace_tokenize,
                remove_stopwords,
                ' '.join,

                clean_html,

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
                remove_long_words,
                remove_empty_tokens,
                ' '.join,


                )


if __name__ == '__main__':
    print(preprocessor(r'''<!-- START YAHOO ANSWERS BADGE -->. <!-- make sure to cut and paste all the badge code -->. <style>. /* . This is the style information that you may edit to change how the badge appears on your web page.. You can change the appearance of just about everything if you'd really like to.  . For more information about CSS, visit http://www.w3schools.com/css/css_intro.asp. Quick Tip: To hide something, just add "display: none;" inside its style definition, without the quotes.  . */. . #ya-badge { border: 1px #54c40b solid; background-color: #fff; width: 163px; padding:0px; font-family:arial; }. #ya-badge #ya-faces { background:url("http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/badge_emoticon.gif"); width: 163px; height:53px; }. #ya-badge a { color:#3499cc!important; text-decoration:none; }. #ya-badge a:hover { color:#006699; text-decoration:underline; }. #ya-badge #ya-badge-content #ya-badge-title { display:block;font-family: arial; font-weight:bold; font-size: 13px; margin-top:5px; margin-left:10px; margin-bottom:5px;}. #ya-badge #ya-badge-content ul { padding:0px!important;margin:0px!important;list-style-type: none!important;padding-left: 0px!important; border:0px!important; background-color: #fff;}. #ya-badge #ya-badge-content ul .ya-listitem { margin-left:10px!important; margin-right:10px!important; list-style-type: none!important; padding: 0px!important; font-family: arial; margin-bottom:3px; padding-bottom:3px; border-bottom:1px #dfdfdf solid; text-indent: 0px!important;}. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-title { font-size: 11px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata {display:block; color: #333; font-size: 9px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata a {color: #333!important; font-size: 9px; }. #ya-badge #ya-badge-content ul .ya-listitem .ya-question-metadata a:hover { color:#006699; text-decoration:underline; }. #ya-badge #ya-more-link { font-size: 10px; text-align:right; display:block; margin:5px; } . #ya-badge #ya-badge-content #ya-level-area { color: #787878; display:block; background:url('http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/pointsstar.gif'); background-repeat:no-repeat; background-position:10px 4px; padding:3px; padding-left:30px; font-size:12px; background-color: #fcfbe7;  }. #ya-badge #ya-badge-content #ya-level-area a { color: #787878!important; }. #ya-badge #ya-badge-content #ya-level-area .ya-level-number { font-weight:bold;  }. #ya-badge #visit-link { margin:5px; margin-left:10px; color:#8b8b8c; font-size:10px; margin-top:5px; }. #ya-badge #visit-link a { color:#8b8b8c!important; text-decoration:underline; }. </style>. . <div id="ya-badge">. <div id="ya-logo"><a href="http://answers.yahoo.com/"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/us/sch/gr/ga_ans_badge.gif"></a></div>. <div id="ya-faces"><a href="http://answers.yahoo.com/question/?link=ask"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a><a href="http://answers.yahoo.com/dir/?link=ask&more=y"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a><a href="http://answers.yahoo.com/dir/?link=over&more=y"><img border="0" src="http://us.i1.yimg.com/us.yimg.com/i/geo/advan/spacer.gif" style="width:54px; height:53px;"></a></div>. . <div id="ya-badge-content">. . <!-- . This is the code that gets the latest information from the Yahoo! Answers servers.  Don't change this unless you really know what you're doing.  . There are some options you may edit at your own risk:. - size:'''))

