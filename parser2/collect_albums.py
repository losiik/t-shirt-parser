import time
import json

import requests
from bs4 import BeautifulSoup

from parser2.collect_categories import collect_categories


BASE_URL = "https://jerseypremium.x.yupoo.com"
urls = collect_categories()
print(urls)

for i in range(len(urls)):
    max_pages = 1

    print(urls[i])
    r = requests.get(f"{BASE_URL}{urls[i]['url']}")
    soup = BeautifulSoup(r.text, 'html.parser')
    print("soup")

    pages = soup.find('nav', class_='pagination__main')
    if pages is not None:
        input_tag = pages.find('input', {'name': 'page'})
        print("input_tag")

        if input_tag and input_tag.has_attr('max'):
            max_pages = int(input_tag['max'])

    print(max_pages)
    urls[i]["max_pages"] = max_pages
    time.sleep(1)


filename = 'data.json'

# Запись массива в файл JSON
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(urls, file, ensure_ascii=False, indent=4)
