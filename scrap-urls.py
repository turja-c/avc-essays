from bs4 import BeautifulSoup
import requests
url = "https://avc.com/archive/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))