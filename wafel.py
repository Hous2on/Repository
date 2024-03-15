import csv

with open('C:/Users/leogo/ИП/Новая папка (2)/Repository/fmlw.csv', encoding= 'utf-8') as f:
    sp = list(csv.DictReader(f, delimiter = ','))
    print(sp[0])