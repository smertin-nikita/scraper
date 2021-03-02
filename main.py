import re

import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


if __name__ == '__main__':
    pattern = re.compile('|'.join(KEYWORDS), re.IGNORECASE)

    response = requests.get(
        url='https://habr.com/ru/all/'
        )
    response.raise_for_status()

    text = response.text

    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article', class_='post post_preview')
    for article in articles:
        if pattern.search(article.text):
            time = article.find('span', class_='post__time').text
            title = article.find('a', class_='post__title_link')
            print(time, title.text, title.get('href'))

