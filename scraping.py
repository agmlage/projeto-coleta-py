from wsgiref import headers
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
idlocalidade=1
board_members = []
#pagini=1
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
#Buscar as UFs no site do correio e salvar em um vetor
def consulta_uf(headers):  
    data = ""
    locais = requests.post(url, headers=headers, data=data)

    soup = BeautifulSoup(locais.text, 'html.parser')

    ufs = soup.find_all("select", { "name" : "UF" })
    for uf in ufs:
        string = uf.text
    lista = string.split()
    #print (lista)
    return lista   

def consulta_cep(uf,idlocalidade):
    print("# UF: " + uf)
    pagini = 1
    while pagini<1100:
        new = 0
        pagfin=pagini+99
        data = "UF="+str(uf)+"&pagini="+str(pagini)+"&pagfim="+str(pagfin)
        resp = requests.post(url, headers=headers, data=data)
        soup = BeautifulSoup(resp.text, 'html.parser')
        tables = soup.find_all("table", { "class" : "tmptabela" })
        for table in tables:
            tabledata= table.find_all ("tr")
            for tr in tabledata:
                tddata = tr.find_all("td")
                if len(tddata)==4:
                    localidade = {
                        "Localidade": tddata[0].text.strip(),
                        "Faixa de CEP": tddata[1].text.strip(),
                        "ID": uf+str(idlocalidade)
                    }
                    skip = False
                    for board_member in board_members:
                        if board_member["Localidade"] == localidade["Localidade"]:
                            skip = True
                            break
                    if not skip:
                        board_members.append(localidade)
                        idlocalidade +=1
                        new += 1
        pagini += 100
        print("\tNew = " + str(new) + "\n\tpagini: " + str(pagini))
        if new == 0:
            break 

def save_json():
    stringfile = ""
    for line in board_members:
        stringfile = stringfile + json.dumps(line,ensure_ascii=False) + "\n"
    with open("ufs.jsonl", "w") as fp:
        fp.write(stringfile)

for uf in consulta_uf(headers):
    consulta_cep(uf,idlocalidade)
#print (board_members)
save_json()