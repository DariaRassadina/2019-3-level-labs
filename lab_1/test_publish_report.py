import unittest
from request import find_articles
from request import publish_report
import json


class MyTestCase(unittest.TestCase):
    def test_publish_report(self):
        url = 'Наука - BBC News Русская служба.html'
        articles = find_articles(open(url).read())
        path = publish_report('/Users/articles.json', articles)
        check_url = False
        check_title = False
        with open(path, 'r') as f:
            data = json.loads(f.read())
            if data['url'] != '0':
                check_url = True
            for i in data['articles']:
                if i['title'] != '0':
                    check_title = True

        self.assertEqual(check_url, True)
        self.assertEqual(check_title, True)


if __name__ == '__main__':
    unittest.main()
