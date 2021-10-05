import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://es.wikipedia.org/wiki/Tom_Felton'
page = requests.get(url)
soup = bs(page.text, "html.parser")
tags = []
for p in soup.find('div', {'class': "mw-parser-output"}).find_all('p')[:-1]:
    tags.append(p.text)
df = pd.DataFrame(tags)
df.to_csv('TomF.txt', sep='\t', encoding='utf-8')
url_page = 'https://www.guiadelocio.com/cine/personajes/tom-felton'
page = requests.get(url_page)
soup = bs(page.text, "html.parser")
info=[]
for t in soup.find('div', {'class': "span12 sinopsis_text"}).find_all('p'):
    info.append(t.text)
df = pd.DataFrame(info)
df.to_csv('TomF2.txt', sep='\t', encoding='utf-8')
print("Se han creado archivos de texto con los resultados obtenidos:)")
