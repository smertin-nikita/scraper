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
    urls = [article.find('a', class_='post__habracut-btn').get('href') for article in articles]

    for url in urls:
        response = requests.get(
            url=url
            )
        response.raise_for_status()

        text = response.text
        bs = BeautifulSoup(text, features='html.parser')
        article = bs.find('article', class_='post post_full')

        if pattern.search(article.text):
            time = article.find('span', class_='post__time').get('data-time_published')
            title = article.find('span', class_='post__title-text').text
            print(time, title, url)

