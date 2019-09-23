import requests

import json

import datetime

from bs4 import BeautifulSoup

from flask import Flask

server = Flask(__name__)


def publish_report(path, articles):
    titles = {}  # should be a list of dictionaries instead
    for i in range(len(articles)):
        titles['title' + str(i + 1)] = articles[i]

    j_file = {'url': path, 'creationDate': datetime.datetime.now().strftime("%Y-%m-%d"), 'articles': titles}

    json_data = json.dumps(j_file)

    with open("articles.json", "w") as file:
        file.write(json_data)


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page)
    head_content = parsed_page.find_all('h3')
    parsed_content = []
    for parsed in head_content:
        titles = parsed.get_text()
        parsed_content.append(titles)
    return parsed_content


@server.route('/')  # start here
def get_html_page(url='https://www.bbc.com/russian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'):
    bbc_science_request = requests.get(url)
    if bbc_science_request.status_code == 200:
        publish_report(url, find_articles(bbc_science_request.text))
        return 'articles.json is created!'


if __name__ == '__main__':
    server.run()
