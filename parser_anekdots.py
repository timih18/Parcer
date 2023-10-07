import requests
from bs4 import BeautifulSoup as BSoup

url = 'https://www.anekdot.ru/last/good/'
r = requests.get(url)
soup = BSoup(r.text, 'html.parser')
text = soup.find_all('div', class_='text')
anekdots = [i.text for i in text]
n = 1
for i in anekdots:
    print(f'{n}. {i}')
    n += 1
