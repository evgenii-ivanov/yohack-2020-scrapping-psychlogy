import datetime
import hashlib
import requests
import codecs
from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

BASE_URL = 'https://twitter.com/'

DIVIDER = "\n=======<>CUSTOM_DIVIDER<>=======\n"

def save_text(text, username):
    if not text.strip():
        return
    with codecs.open('texts/' + username + '.txt', 'a', 'utf-8') as file:
        file.write(text.strip())
        file.write(DIVIDER)

def get_posts(username):
    browser.get(BASE_URL + username)
    sleep(5)
    browser.execute_script("window.scrollTo(0, 1000)")
    sleep(4)
    outer_block = 'div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0'
    posts = browser.find_elements_by_css_selector(outer_block + ' > span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0')
    for post in posts:
        save_text(post.text, username)

def get_posts_from_file(username):
    with codecs.open('texts/' + username + '.txt', 'r', 'utf-8') as file:
        buffer = file.read()
        return buffer.split(DIVIDER)[:-1]


get_posts('digitalskynet1')
print(get_posts_from_file('digitalskynet1'))