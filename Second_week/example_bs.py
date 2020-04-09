import requests
import re
from bs4 import BeautifulSoup

resp = requests.get("https://wikipedia.org/")
html = resp.text
"""Поиск ссылок на проекты Википедии с помощью регулярных выражений"""
links = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
print(links)
"""Поиск ссылок на проекты Википедии с помощью BeautifulSoup"""
soup = BeautifulSoup(html, 'lxml')  # Распарсили страницу
tags = soup('a', 'other-project-link')  # Нашли все объекты с тэгом а и other-project-link'
links_1 = [tag['href'] for tag in tags]  # Создали список ссылок
print(links_1)
