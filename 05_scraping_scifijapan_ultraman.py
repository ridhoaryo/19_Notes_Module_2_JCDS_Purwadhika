import requests
from bs4 import BeautifulSoup

web = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = BeautifulSoup(web.content, 'html.parser')

div = data.find('div', class_='entry')
div_strong = div.find_all('strong')
ultraman_list = []
monster_list = []
for i in div_strong:
    ultraman_list.append(i.text)
ultraman = ultraman_list[2:36]
monster = ultraman_list[37:110]
print('Ultraman List: ')
print(ultraman)
print('\n')
print('Monster List: ')
print(monster)