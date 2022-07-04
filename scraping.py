import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#Buscar as UFs no site do correio e salvar em um vetor
url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
id=1
board_members = []

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = ""
locais = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(locais.text, 'html.parser')

ufs = soup.find_all("select", { "name" : "UF" })
for uf in ufs:
    string = uf.text
lista = string.split()

#Percorrer o vetor buscando informações das UFs
for cont in range (2):
    data = "UF="+lista[cont]
    
    resp = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tables = soup.find_all("table", { "class" : "tmptabela" })
    for table in tables:
        
        tabledata= table.find_all ("tr")
    for tr in tabledata:
        tddata = tr.find_all("td")
        if len(tddata)==4:
            board_members.append((lista[cont],tddata[0].text.strip(), tddata[1].text.strip(),id))
            id +=1

    board_array = np.asarray(board_members)
    len(board_array)
    df = pd.DataFrame(board_array)
    df.columns = ['UF','Localidade', 'Faixa de CEP','id']
    df.to_csv('\Projeto\projeto-coleta-py\members.csv')
    