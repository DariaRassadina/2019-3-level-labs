import request as parser
from flask import Flask, render_template

server = Flask(__name__)


@server.route('/')
def main():
    url = 'file:///Users/dasa/Desktop/Наука%20-%20BBC%20News%20Русская%20служба.htm'
    html_page = parser.get_html_page(url)
    articles = parser.find_articles(html_page)
    json_file = parser.publish_report('/Users/articles.json', articles)  # returns file's path
    return "json was created"


# return render_template('list_of_articles.html', parser.publish_report('/Users/articles.json', articles))


if __name__ == '__main__':
    server.run()
