import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://jerseypremium.x.yupoo.com"

filename = 'data.json'
with open(filename, 'r', encoding='utf-8') as file:
    urls = json.load(file)


for i in range(len(urls)):

    albums_urls = []
    page_amount = urls[i]["max_pages"]
    print(page_amount)
    for j in range(1, page_amount + 1):
        try:
            r = requests.get(f"{BASE_URL}{urls[i]['url']}?page={j}")

            soup = BeautifulSoup(r.content, 'html.parser')

            # Поиск всех ссылок внутри дочерних элементов
            links = soup.find_all('a', class_='album__main')

            # Извлечение URL ссылок
            albums_urls += [{"url": link['href'], "title": link['title']} for link in links]
            print(albums_urls)
            print(len(albums_urls))
            print(j)
        except Exception as e:
            print(e)

    urls[i]["albums_url"] = albums_urls
    print(albums_urls)
    print(len(albums_urls))

filename = 'albums.json'

# Запись массива в файл JSON
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(urls, file, ensure_ascii=False, indent=4)
