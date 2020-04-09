import requests
from bs4 import BeautifulSoup


# Работа через API с сайтом ЦБ
resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(resp.content, 'xml')
print("EUR: ", soup.find('CharCode', text='EUR').find_next_sibling('Value').string)  # Вывод курса евро
print("USD: ", soup.find('CharCode', text='USD').find_next_sibling('Value').string)  # Вывод курса доллара
print("GBP: ",  soup.find(ID="R01035").Value.string)  # Вывод курса фунта стерлингов по ID
