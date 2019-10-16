import unittest
from request import get_html_page


class MyTestCase(unittest.TestCase):
    def test_html_page(self):
        url = 'https://www.bbc.com/russian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'
        a = get_html_page(url)
        print(a)
        self.assertEqual(a.status_code, 200)


if __name__ == '__main__':
    unittest.main()
