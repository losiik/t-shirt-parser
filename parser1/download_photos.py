import os
import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://minkang.x.yupoo.com"

filename = 'albums.json'
with open(filename, 'r', encoding='utf-8') as file:
    albums = json.load(file)

image_urls = [
    "https://s.yupoo.com/website/4.25.7/icons/logo1@558.png",
    "https://s.yupoo.com/website/4.25.7/imgs/logo_3.png",
    "https://pic.yupoo.com/minkang/2d5517af/medium.jpeg",
    "https://pic.yupoo.com/minkang/a04daed0/small.png",
    "https://pic.yupoo.com/minkang/da4ac08c/small.png",
    "https://pic.yupoo.com/minkang/0352bad1/small.jpeg",
    "https://pic.yupoo.com/minkang/67d5e380/small.jpeg",
    "https://pic.yupoo.com/minkang/2d5517af/small.jpeg",
    "https://pic.yupoo.com/minkang/a7643fa6/small.jpeg",
    "https://pic.yupoo.com/minkang/0719d246/small.jpeg",
    "https://pic.yupoo.com/minkang/127fcb60/small.jpeg",
    "https://pic.yupoo.com/minkang/6df5bb60/small.jpeg",
    "https://pic.yupoo.com/minkang/b9de73fa/small.jpeg",
    "https://s.yupoo.com/website/4.25.7/imgs/policeIcon.png",
    "https://s.yupoo.com/website/4.25.7/icons/logo1@558.png",
    "https://s.yupoo.com/website/4.25.7/imgs/logo_3.png",
    "https://pic.yupoo.com/minkang/9a4c6eaf/medium.jpeg",
    "https://pic.yupoo.com/minkang/1f8c3373/small.jpeg",
    "https://pic.yupoo.com/minkang/d7cea219/small.jpeg",
    "https://pic.yupoo.com/minkang/ac1faf88/small.jpeg",
    "https://pic.yupoo.com/minkang/3af7c4dd/small.jpeg",
    "https://pic.yupoo.com/minkang/9a4c6eaf/small.jpeg",
    "https://pic.yupoo.com/minkang/e414dc76/small.jpeg",
    "https://pic.yupoo.com/minkang/14ffdfa7/small.jpeg",
    "https://pic.yupoo.com/minkang/f26ec59a/small.jpeg"
]

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

            if img not in image_urls:
                try:
                    img_response = requests.get(img)
                    with open(f'{album["title"]}/{title}/{j}.jpg', 'wb') as img_file:
                        img_file.write(img_response.content)
                except Exception as e:
                    print(e)


