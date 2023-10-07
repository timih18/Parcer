import requests
from bs4 import BeautifulSoup as BSoup

url = 'https://www.perekrestok.ru/cat/c/366/ovosi-zelen-griby'
responce = requests.get(url).text
soup = BSoup(responce, 'html.parser')
text_products = soup.find_all('span', class_='product-card__link-text')
products = [i.text for i in text_products]
text_prices = soup.find_all('div', class_='price-new')
prices = [i.text for i in text_prices]
clear_prices = []
for i in prices:
    clear_price = i[:i.find('\xa0₽')]
    clear_prices.append(clear_price+'₽')
# print(products)
# print(prices)
# print(len(products))
# print(len(prices))
# print(len(clear_prices))
need_product = input()
for i in products:
    if need_product in i:
        index = products.index(i)
        print(i, '|', clear_prices[index])