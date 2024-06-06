import requests
from bs4 import BeautifulSoup


def collect_categories():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Cookie': 'language=ru; Hm_lvt_28019b8719a5fff5b26dfb4079a63dab=1716897848; _ga=GA1.1.321143664.1716990208; Hm_lpvt_28019b8719a5fff5b26dfb4079a63dab=1717037763; _ga_XMN82VEYLV=GS1.1.1717034646.2.1.1717037763.0.0.0',
        'If-None-Match': 'W/"2bde9-DctPZogQ6HZCfwVuJcSoPS4mI7Q"',
        'Priority': 'u=0, i',
        'Referer': 'https://minkang.x.yupoo.com/categories/664377',
        'Sec-Ch-Ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    r = requests.get("https://minkang.x.yupoo.com/categories", headers=headers)
    print(r)

    soup = BeautifulSoup(r.content, 'html.parser')

    # Поиск элемента с классом 'categories__box-left'
    box_left = soup.find('div', class_='categories__box-left')

    # Поиск всех ссылок внутри дочерних элементов
    links = box_left.find_all('a', href=True)

    # Извлечение URL ссылок
    urls = [{"url": link['href'], "title": link.text} for link in links]

    urls.pop(0)

    for i, url in enumerate(urls):
        if url["title"] == "🇯🇵Japan League":
            urls = urls[:i + 1]

    return urls
