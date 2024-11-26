import requests
import csv

from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

news = soup.find_all('div', class_='sc-b8778340-3 gxEarx') 
data = []

for new in news:
    title = new.find('h2').text
    story = new.find('p').text
    if title and story:
        data.append([title, story])

# Write to CSV
with open('brokennews.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Story"])
    writer.writerows(data)

print("Data saved to 'brokennews.csv'.")



# <div data-testid="card-text-wrapper" class="sc-b8778340-3 gxEarx">grid
# <div data-testid="card-text-wrapper" class="sc-b8778340-3 gxEarx">…</div>grid

# <h2 data-testid="card-headline" class="sc-8ea7699c-3 dhclWg">
# <h2 data-testid="card-headline" class="sc-8ea7699c-3 dhclWg">

# <p data-testid="card-description" class="sc-b8778340-4 kYtujW">
# <p data-testid="card-description" class="sc-b8778340-4 kYtujW">
