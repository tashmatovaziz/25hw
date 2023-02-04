import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.gismeteo.ru/weather-bishkek-5327/now/"

HEADERS = {
    'Accept': 'text/html,appliction/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X21; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_='now')
    weather = {
        "date": item.find('div', class_='now-localdate').string,
        "link": f"https://www.gismeteo.ru/weather-bishkek-5327/now/",
        "astro-sunrise": item.find('div', class_='now-astro-sunrise').text,
        "astro-sunset": item.find('div', class_='now-astro-sunset').text,
        "now-weather": item.find('div', class_='now-weather').text,
        "now-feel": item.find('div', class_='now-feel').text,
        "now-desc": item.find('div', class_='now-desc').text,
        "now-info-item wind": item.find('div', class_='now-info-item wind').text,
        "now-info-item humidity": item.find('div', class_='now-info-item humidity').text

    }
    return weather


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        weather = get_data(html.text)
        return weather
    else:
        raise Exception("Error in parser!")