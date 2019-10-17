import unittest
from request import find_articles
from request import publish_report
import json


class MyTestCase(unittest.TestCase):
    def test_publish_report(self):
        url = 'Наука - BBC News Русская служба.html'
        articles = find_articles(open(url).read())
        path = publish_report('articles.json', articles)
        with open(path, 'r') as f:
            data = json.loads(f.read())
            self.assertTrue(len(data['url']) > 1)
            for i in data['articles']:
                for k in i:
                    self.assertIsNotNone(i[k])


if __name__ == '__main__':
    unittest.main()
