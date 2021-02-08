import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
print(r.status_code)

soup = BeautifulSoup(r.text)
#print(soup)

for text in soup.find_all('p'):
    print(text)

