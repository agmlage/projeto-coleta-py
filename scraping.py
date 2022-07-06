from wsgiref import headers
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
#from pyoccur import pyoccur

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
id=1
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
    

def consulta_cep(uf,id,url,headers):
    #Percorrer o vetor buscando informações das UFs
    for cont in range (20):
        lista=uf
        pagfin=pagini+99
        #data = "UF="+lista[cont]+"&pagini="+str(pagini)+"&pagfim="+str(pagfin)
        data = "UF=SP"+"&pagini="+str(pagini)+"&pagfim="+str(pagfin)

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

def teste(uf,id,url,headers):
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
            board_members.append((str(uf),tddata[0].text.strip(), tddata[1].text.strip(),id))
            id +=1
    board_array = np.asarray(board_members)
    len(board_array)
    #print (board_array)
    df = pd.DataFrame(board_array)
    #print (df)
    df.columns = ['UF','Localidade', 'Faixa de CEP','id']
    #df.drop_duplicates(subset='Localidade')
    #print(df)
    #return df
    df.to_csv('\Projeto\projeto-coleta-py\members.csv')
    return id
def repini(pagini,uf,id,url,headers):
    while pagini<900:
        var=teste(uf,id,url,headers)
        pagini+=100
    return var

lista=consulta_uf(headers)
#print(lista)
#df=teste(consulta_uf(headers),id,url,headers)
for cont in range (len(lista)):
    uf=lista[cont]
    print (uf)
    pagini=1
    id=repini(pagini,uf,id,url,headers)
