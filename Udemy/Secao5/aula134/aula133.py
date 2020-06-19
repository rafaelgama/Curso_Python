# Web Scraping com Python.
# instalar os pacotes: pip install requests e beautifulsoup4

import requests # parar fazer as requisições
from bs4 import BeautifulSoup # Para permitir manipular o html.

url = 'https://pt.stackoverflow.com/questions/tagged/python'

# pegar a respota do request
response = requests.get(url)
#print(response.text) # mostra o html da pagina
# Analisar o HTML e disponibilizar o Objeto
html = BeautifulSoup(response.text, 'html.parser')

# select() = seletor CSS do BeautifulSoup
for pergunta in html.select('.question-summary'):
    # select_one() = seletor CSS do BeautifulSoup para um só
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')
    # pega somente os textos da tag do CSS ex: "objeto".text
    print(titulo.text, data.text, votos.text, sep='\t')






