from html_parser import process_hn_page, replace_6_len_words
from bs4 import BeautifulSoup


def test_put_tm_sign():
    with open("resource/1.html") as f:
        html = f.read()
    res = process_hn_page(html)
    with open("resource/out_1.html") as f:
        res_html = f.read()
    assert str(BeautifulSoup(res_html)) == str(BeautifulSoup(res))


def test_dash():
    with open("resource/2.html") as f:
        html = f.read()
    res = process_hn_page(html)
    with open("resource/out_2.html") as f:
        res_html = f.read()
    assert str(BeautifulSoup(res_html)) == str(BeautifulSoup(res))


def test_link_sub():
    with open("resource/3.html") as f:
        html = f.read()
    res = process_hn_page(html)
    with open("resource/out_3.html") as f:
        res_html = f.read()
    assert str(BeautifulSoup(res_html)) == str(BeautifulSoup(res))


def test_replace_in_string():
    ret = replace_6_len_words("mighty booshe")
    assert ret == "mighty™ booshe™"
