import unittest
from request import find_articles


class MyTestCase(unittest.TestCase):

    def test_number_of_articles(self):
        url = 'Наука - BBC News Русская служба.html'
        length_of_dict = len(find_articles(open(url).read()))
        self.assertEqual(length_of_dict, 26)


if __name__ == '__main__':
    unittest.main()
