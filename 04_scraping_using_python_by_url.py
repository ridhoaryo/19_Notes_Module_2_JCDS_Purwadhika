import requests
from bs4 import BeautifulSoup
web = requests.get('http://127.0.0.1:5500/01_learning_html.html')
data = BeautifulSoup(web.content, 'html.parser')

ul = data.ul
for i in ul.find_all('li', id = 'person'):
    print(i.text)