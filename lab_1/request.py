import requests

from bs4 import BeautifulSoup

page_url = 'https://www.bbc.com/russian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'

bbc_science_request = requests.get(page_url)

bbc_science_content = bbc_science_request.text

parsed_page = BeautifulSoup(bbc_science_content)

print(parsed_page.title.text)

print(parsed_page.find_all('h3'))






