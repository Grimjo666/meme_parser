from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from time import sleep

ua = UserAgent().random
headers = {"UserAgent": ua}


def get_links_on_page_memes():
    response = requests.get("https://memepedia.ru/memoteka/", headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    list_memes = soup.find_all("li", class_="post-item post-item-masonry-boxed")

    for item in list_memes:
        url = item.find("a").get("href")
        yield url
        sleep(0.3)


for link in get_links_on_page_memes():
    res_page = requests.get(link, headers=headers)
    soup_page = BeautifulSoup(res_page.text, "lxml")

    meme_name = soup_page.find("h1", class_="entry-title s-post-title bb-mb-el")
    meme_pic = soup_page.find("figure", class_="post-thumbnail").find("img").get("src")
    description = soup_page.find("div", class_="js-mediator-article").find("p").text
    origin = ''.join([p.text for p in soup_page.find_all("h2")[1].find_all_next("p")[:3]])
