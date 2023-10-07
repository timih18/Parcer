import requests
from bs4 import BeautifulSoup as BSoup

url = 'https://www.goodreads.com/quotes?page=1'
r = requests.get(url)
soup = BSoup(r.text, 'html.parser')
text_quotes = soup.find_all('div', class_='quoteText')
quotes = [i.text for i in text_quotes]
text_authors = soup.find_all('span', class_='authorOrTitle')
authors = [i.text for i in text_authors]
c = 0
for i in quotes:
    fcomma = i.find('“')
    lcomma = i.rfind('”')
    clear_quote = i[fcomma:lcomma+1]
    print(f'{c+1}.', clear_quote, authors[c])
    c+=1