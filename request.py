import requests

import json

import datetime

from bs4 import BeautifulSoup


def publish_report(path, articles):
    dictionary_for_json = {'url': 'https://www.bbc.com/russian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53',
                           'creationDate': datetime.datetime.now().strftime("%Y-%m-%d"),
                           'articles': articles}
    with open(path, "w") as file:
        file.write(json.dumps(dictionary_for_json, ensure_ascii=False))
    return path


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page)
    head_content = parsed_page.find_all('h3', {"class": "title-link__title"})
    parsed_titles = []
    for parsed in head_content:
        dic = {'title': parsed.get_text(), 'time': datetime.datetime.now().strftime("%H:%M:%S")}
        parsed_titles.append(dic)
    return parsed_titles


def get_html_page(url):
    bbc_science_request = requests.get(url)
    return bbc_science_request
