import pandas as pd
from bs4 import BeautifulSoup

html = open("D:\\Мамочка\\аксиома\\ЕГИССО\\akt.xls",'rb').read().decode('utf-8', 'ignore')
table = BeautifulSoup(html, 'html.parser').find('table')
# print(table)
df = pd.read_html(str(table)) #I think it accepts BeatifulSoup object

df = df[0]

# clear_data = df[[0,4]][:-2]
# clear_data.to_csv('test.csv', encoding='cp1251', sep=';')
D = pd.Series(df[[0,4]][:-2])