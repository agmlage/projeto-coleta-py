import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = ""

resp = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(resp.text, 'html.parser')

ufs = soup.find_all("select", { "name" : "UF" })
for uf in ufs:
    print(uf.text)



