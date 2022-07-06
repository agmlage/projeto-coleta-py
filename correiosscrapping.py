import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
pagini=1

def consulta_cep(pagini):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    
    pagfin=pagini+99


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
    return td.text

while pagini<900:
    consulta_cep(pagini)
    pagini+=100