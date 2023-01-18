from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from time import sleep

ua = UserAgent().random
headers = {"UserAgent": ua}


def get_links_on_page_memes():
    response = requests.get("https://memepedia.ru/memoteka/", headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    list_memes = soup.find_all('li', class_='post-item post-item-masonry-boxed')

    for item in list_memes:
        url = item.find('a').get('href')
        yield url
        sleep(0.3)

