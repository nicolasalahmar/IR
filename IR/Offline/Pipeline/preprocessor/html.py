import re
from bs4 import BeautifulSoup

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
HTML_TAG_PATTERN = re.compile(r'<[^>]+>')

def clean_html(text):
    try:
        if not BeautifulSoup(text, "html.parser").find():
          return text
        soup = BeautifulSoup(text, "html.parser")
        [s.extract() for s in soup('style')]
        html = str(soup)
        cleaned_text = re.sub(CLEANR, '', html)
        return cleaned_text
    except:
        return text
