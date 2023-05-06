import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Find all the images on the page
images = soup.find_all('img')
for image in images:
    print(image.get('src'))


