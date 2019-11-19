# WEB SCRAPING
# Take data from digidb.io (Digimon database website) and save it to .csv, .json, .xlsx

Halo, assalamu'alaykum..

Hari ini saya akan menjelaskan tentang pelajaran yang saya terima hari ini, yaitu tentang Web Scraping. Di materi ini, kita diberi quiz, untuk mengambil data dari database website Digimon.

![alt text](http://digidb.io/images/dot/dot151.png "Logo Title Text 1")

Untuk file coding bisa dilihat di:
- **06_scraping_digimondb.py**

Untuk file excel, json dan csv:
- **Digimon.xlsx**
- **Digimon.json**
- **Digimon.csv**

## Let's brakedown the code
## 1. Import the Library
```
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import csv
import json
```
## 2. Request the url and preparing the sector we are gonna get
```
web = requests.get('http://digidb.io/digimon-list/')
data = BeautifulSoup(web.content, 'html.parser')

table = data.find('table', id='digiList')
tbody = table.find('tbody')
img = tbody.find_all('img')
```
Maksudnya, dari `data` cari `table` dengan `id` `digiList`. Kemudian dari `table`, cari `tbody`. Terakhir daro `tbody` cari semua `img`.
## 3. Make list for header only
```
header_list = []
header = table.find('tr', class_='header')

th = header.find_all('th')
for i in th:
    header_list.append(i.text)
header_list.append('Image link')
```
## 4. Make list of image link
```
image_list = []
for i in img:
    image_list.append(i['src'])

```
## 5. Make list of digimon's name
```
digimon_list = []
digi = tbody.find_all('a')
for i in digi:
    digimon_list.append(i.text)
```
## 6. Make list of number
```
number_list = []
for i in range(1,len(digimon_list)+1):
    number_list.append(i)
```
## 7. Make list of attribute
```
attribute_list = []
att = tbody.find_all('center')
for i in att:
    attribute_list.append(i.text)
```
## 8. Grouping the attributes
```
grouped_attributes = []
j = 0
for i in range(11,3762,11):
    grouped_attributes.append(attribute_list[j:i])
    j += 11
```
## 9. Append and insert another list into grouped_attributes
```
for i in range(len(grouped_attributes)):
    grouped_attributes[i].append(image_list[i])
    grouped_attributes[i].insert(0,digimon_list[i])
    grouped_attributes[i].insert(0,number_list[i])
```
## 10. Lastly, insert header_list
```
grouped_attributes.insert(0, header_list)
```
## 11. Write to .xlsx
```
digimon_xlsx = xlsxwriter.Workbook('Digimon.xlsx')
sheet1 = digimon_xlsx.add_worksheet('Digimon List')
for r in range(len(grouped_attributes)):
    for c in range(len(header_list)):
        sheet1.write(r,c,grouped_attributes[r][c])

digimon_xlsx.close()
```
## 12. Make the data as json format
```
digimon_all = []
header_only = grouped_attributes[0]
content = grouped_attributes[1:]
for i in range(len(content)):
    data = dict(zip(header_only, content[0:][i]))
    digimon_all.append(data)

print(digimon_all[0])
```
## 13. Write to json
```
with open('Digimon.json', 'w') as my_digimon:
    json.dump(digimon_all, my_digimon)
```
## 14. Write to csv
```
with open('Digimon.csv', 'w', newline='') as digimon_csv:
    column = header_only
    write = csv.DictWriter(digimon_csv, fieldnames=column)
    write.writeheader()
    write.writerows(digimon_all)
```

Sekian dan terimakasih