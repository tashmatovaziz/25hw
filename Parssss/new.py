import mport as mport
import requests as requests

import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://hezka.ag/new/"

HEADERS = {
    'Accept': 'bext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozila/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    films = []
    for item in items:
        info = item.find('div', class_="b-content__inline_item-link").find('div').string.split(', ')
        film = {
            'title': item.find('div', class_="b-content__inline_item-link").find('a').string,
            'link': item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            'date': info[0],
            'country': info[1],
            'genre': info[2]
        }
        films.append(film)
    return films


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = get_data(html.text)
        return films
    else:
        raise Exception("Error in parser!")