import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = ""
locais = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(locais.text, 'html.parser')

ufs = soup.find_all("select", { "name" : "UF" })
for uf in ufs:
    string = uf.text
    #output=string.split(' ')
    #output
    #print(string)
lista = string.split()
#print (lista)

for cont in range(len(lista)):
    print (cont,lista[cont])
