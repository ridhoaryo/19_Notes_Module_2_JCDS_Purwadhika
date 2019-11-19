from bs4 import BeautifulSoup

data = BeautifulSoup(open('01_learning_html.html', 'r'), 'html.parser')

print(data.find(class_ = 'orang'))
print(data.find('li', class_='orang'))

ul = data.ul
for i in ul.find_all('li', class_ = 'orang'):
    print(i.text) 