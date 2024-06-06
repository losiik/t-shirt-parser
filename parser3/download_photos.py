import os
import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://classic-football-fhirts052.x.yupoo.com"

filename = 'albums.json'
with open(filename, 'r', encoding='utf-8') as file:
    albums = json.load(file)

for album in albums:
    try:
        os.makedirs(album["title"])
    except:
        continue

    for i, url in enumerate(album["albums_url"]):
        title = url["title"].replace("/", "_")
        title = title.replace(" ", "_")
        title = title.replace(":", "_")
        try:
            os.makedirs(f'{album["title"]}/{title}')
        except:
            try:
                title += f"{i}"
                os.makedirs(f'{album["title"]}/{title}')
            except:
                break

        try:
            r = requests.get(f'{BASE_URL}{url["url"]}')
        except Exception as e:
            print(e)
            break

        soup = BeautifulSoup(r.text, 'html.parser')

        # Поиск всех тегов <img>
        img_tags = soup.find_all('img')

        # Список для хранения ссылок на изображения
        img_urls = []

        # Извлечение ссылок на изображения
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                if img_url.endswith(('.jpg', '.jpeg', '.png')):
                    img_urls.append(img_url)

        for j, img in enumerate(img_urls):
            if not img.startswith('https'):
                img = "https:" + img
            img = img.replace("photo", "pic")

            print(img)

            try:
                img_response = requests.get(img)
                with open(f'{album["title"]}/{title}/{j}.jpg', 'wb') as img_file:
                    img_file.write(img_response.content)
            except Exception as e:
                print(e)


