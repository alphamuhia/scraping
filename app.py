import requests
import csv

from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')


# print(response.status_code)

# print(soup)
# h1_tags = soup.find_all('h1')

# print(h1_tags)

# for h1_tag in h1_tags:
#     print(h1_tag.text)
    # print(hi_tags)

books = soup.find_all('article', class_='product_pod')

# print(books)
data = []

for book in books[:5]:
    title = book.h3.a['title']
    price = book.find('p', class_="price_color").text
    availability = book.find('p', class_="instock availability").text.strip()
    data.append({title, price, availability})
    # print(title)



    # with open('bookstore.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Title", "Price", "Availability"])
    #     writer.writerows(data)