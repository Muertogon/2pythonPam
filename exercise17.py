import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
print(r.status_code)

soup = BeautifulSoup(r.text)
#print(soup)

for story_heading in soup.find_all(class_="balancedHeadline"):

    print(story_heading)
