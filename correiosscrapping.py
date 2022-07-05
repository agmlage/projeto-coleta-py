import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

pagini=1
pagfin=100


data = "UF=SP"+"&pagini="+str(pagini)+"&pagfim="+str(pagfin)


resp = requests.post(url, headers=headers, data=data)


soup = BeautifulSoup(resp.text, 'html.parser')

tables = soup.find_all("table", { "class" : "tmptabela" })
for table in tables:
    print("\n\n\n")
    tabledata= table.find_all ("tr")
    for tr in tabledata:
        tddata = tr.find_all("td")
        print("\n>>")
        for td in tddata:
            print(td.text)


while pagfin < 900:
    pagini+=100
    pagfin+=100