import csv

products = []
prices = []
with open('csv_links_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        products.append(row['name'])
with open('csv_prices.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        prices.append(row['price'])
need_product = input()
for elem in products:
    if need_product in elem:
        index = products.index(elem)
        print(elem, '|', prices[index])