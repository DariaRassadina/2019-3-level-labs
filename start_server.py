import request as parser
from flask import Flask, render_template, redirect, url_for
import json

server = Flask(__name__)


@server.route('/', methods=['GET'])
def main():
    url = 'https://www.bbc.com/russian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'
    html_page = parser.get_html_page(url)
    articles = parser.find_articles(html_page.text)
    json_file_path = parser.publish_report('articles.json', articles)
    file = open(json_file_path, encoding='UTF-8')
    json_string = file.read()
    file.close()
    dictionary_json = json.loads(json_string)
    return render_template('list_of_articles.html', data=dictionary_json)


@server.route('/refresh', methods=['POST'])
def update_page():
    return redirect(url_for('main'))


if __name__ == '__main__':
    server.run()
