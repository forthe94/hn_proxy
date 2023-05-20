from bs4 import BeautifulSoup, dammit
from bs4.formatter import HTMLFormatter
import re

import config

formatter = HTMLFormatter(entity_substitution=dammit.EntitySubstitution.substitute_html)


def replace_6_len_words(string: str):
    return re.sub(r"\b(\w{6})\b", r"\1™", string)


def replace_links(string: str):
    return re.sub(rf"{config.HACKERNEWS_URL}", r"localhost:8000", string)


def process_hn_page(html: str) -> str:
    soup = BeautifulSoup(html)
    items = [soup.find("html")]

    if items[0] is None:
        return html

    texts = soup.findAll(text=True)

    for text in texts:
        if text.parent.name in ["a"]:
            continue
        replace_text = replace_links(text)
        replace_text = replace_6_len_words(replace_text)
        text.replace_with(replace_text)

    return soup.prettify(formatter=formatter)
