import request as parser
from flask import Flask, render_template
import json

server = Flask(__name__)


@server.route('/')
def main():
    url = 'Наука - BBC News Русская служба.html'
    html_page = parser.get_html_page(url)
    articles = parser.find_articles(html_page)
    json_file_path = parser.publish_report('/Users/articles.json', articles)  # returns file's path
    file = open(json_file_path, encoding='UTF-8')
    json_string = file.read()
    file.close()
    dictionary_json = json.loads(json_string)
    return render_template('list_of_articles.html', data=dictionary_json)


if __name__ == '__main__':
    server.run()
