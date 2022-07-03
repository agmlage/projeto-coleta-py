import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import pandas as pd

#Buscar as UFs no site do correio e salvar em um vetor
url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

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
for cont in range (1):
    data = "UF="+lista[cont]
    #print (data)
    resp = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tables = soup.find_all("table", { "class" : "tmptabela" })
    for table in tables:
        #print("\n\n\n")
        tabledata= table.find_all ("tr")
    for tr in tabledata:
        tddata = tr.find_all("td")
        print("\n>>")
        for td in tddata:
            print(td.text)

    