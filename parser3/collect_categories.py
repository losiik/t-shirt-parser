import requests
from bs4 import BeautifulSoup


def collect_categories():

    r = requests.get("https://classic-football-fhirts052.x.yupoo.com/categories")
    print(r)

    soup = BeautifulSoup(r.content, 'html.parser')

    # Поиск элемента с классом 'categories__box-left'
    box_left = soup.find('div', class_='categories__box-left')

    # Поиск всех ссылок внутри дочерних элементов
    links = box_left.find_all('a', href=True)

    # Извлечение URL ссылок
    urls = [{"url": link['href'], "title": link.text} for link in links]

    urls.pop(0)

    return urls
