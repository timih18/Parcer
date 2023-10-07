# Некорректно выводит некоторые цены
import requests
import csv
from bs4 import BeautifulSoup as BSoup


prices = []
urls = []
with open('csv_links_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        urls.append(row['link'])
for url in urls:
    response = requests.get(url)
    soup = BSoup(response.text, 'html.parser')
    text_price_not_clear = soup.find('div', class_='price-new')
    text_price = [i.text for i in text_price_not_clear]
    price_not_clear = text_price[0]
    price = price_not_clear[:price_not_clear.find('\xa0₽')]
    prices.append(price)
with open('csv_prices.csv', 'w',  newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['price'])
    for price in prices:
        writer.writerow([price])