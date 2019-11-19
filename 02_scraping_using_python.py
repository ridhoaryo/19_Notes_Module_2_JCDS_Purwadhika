from bs4 import BeautifulSoup
# web scraping from html file
data = BeautifulSoup(open('01_learning_html.html', 'r'), 'html.parser')
print(data.prettify())
print(data.title)
print('using title.text:', data.title.text)
print('using title.string:', data.title.string)
print('using title.name:', data.title.name) # to get tag
print('\n')
print('using h1.text:', data.h1.text)
print('using h1.string:', data.h1.string)
print('using h1.name:', data.h1.name) # to get tag
print('\n')
print('using ul.text:', data.ul.text)
print('using ul.string:', data.ul.string)
print('using ul.name:', data.ul.name)
print('\n')
print('using data.find_all:', data.find_all('li'))
print('\n')
for x in data.find_all('li'):
    print(x.text)

ul = data.ul
for i in ul.find_all('li'):
    print(i.text)