from bs4 import BeautifulSoup, dammit
from bs4.formatter import HTMLFormatter
import re

import config

formatter = HTMLFormatter(entity_substitution=dammit.EntitySubstitution.substitute_html)


def replace_6_len_words(string: str):
    return re.sub(r"\b(\w{6})\b", r"\1™", string)


def process_hn_page(html: bytes) -> bytes:
    soup = BeautifulSoup(html)
    items = [soup.find("html")]

    if items[0] is None:
        return html

    texts = soup.findAll(text=True)

    for text in texts:
        replace_text = replace_6_len_words(text)
        text.replace_with(replace_text)

    for a in soup.find_all(href=True):
        a['href'] = a['href'].replace(config.HACKERNEWS_URL, 'localhost:8000')

    return soup.encode('utf-8', formatter=formatter)
