import requests
from bs4 import BeautifulSoup
import re

def obter_data_filme_imdb(titulo_filme):
    url_busca = f'https://www.imdb.com/find?q={titulo_filme.replace(" ", "+")}&s=tt&ttype=ft&ref_=fn_ft'
    response_busca = requests.get(url_busca)
    soup_busca = BeautifulSoup(response_busca.text, 'html.parser')

  
    link_primeiro_filme = soup_busca.find('td', class_='result_text').a['href']
    
    url_filme = f'https://www.imdb.com{link_primeiro_filme}'
    response_filme = requests.get(url_filme)
    soup_filme = BeautifulSoup(response_filme.text, 'html.parser')
    
   
    data_lancamento = soup_filme.find('a', {'title': 'See more release dates'}).get_text()
    
    return data_lancamento.strip()

titulo_filme = input("Digite o título do filme: ")
data_filme = obter_data_filme_imdb(titulo_filme)

print(f"A data de lançamento de '{titulo_filme}' é: {data_filme}")