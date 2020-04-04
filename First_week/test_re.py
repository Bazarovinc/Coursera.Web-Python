import re
import requests

res = requests.get("https://cbr.ru")  # Гет-запрос с сайта Цб
html = res.text  # Преобразуем в текст
f_e = re.search(r'евро\D+(\d+,\d+)', html, re.IGNORECASE)  # Находим слово Евро и запоминаем цифры игнорируя регистр
euro = f_e.group(1)  # Выделяем только цифры(курс евро)
print(euro)
f_d = re.search(r'Доллар\D+(\d+,\d+)', html)  # Находим слово Доллар и запоминаем цифры
dollar = f_d.group(1)  # Выделяем только цифры(курс доллар)
print(dollar)

# Looking for car number

text = 'Черная ТОЙОТА КАМРИ с госномером А777АА777' \
       'Белый ВОЛКСВАГЕН ГОЛЬФ с госномером А228РР123' \
       'Красная ЛАДА ПРИОРА с госномером Р001РР01'
pattern = r'[АУКЕНХОРВСМТ]\d{3}[АУКЕНХОРВСМТ]{2}\d{2,3}'
print(re.findall(pattern, text))
