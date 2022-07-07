from wsgiref import headers
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import json

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
idlocalidade=1
board_members = []
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

def consulta_uf(headers):   #Buscar as UFs inseridas no select do site e salvar em um vetor
    data = ""
    locais = requests.post(url, headers=headers, data=data)

    soup = BeautifulSoup(locais.text, 'html.parser')

    ufs = soup.find_all("select", { "name" : "UF" })
    for uf in ufs:
        string = uf.text
    lista = string.split()
    #print (lista)
    return lista   



def consulta_cep(uf,idlocalidade):  #Percorrer o vetor das UFs buscando todos os CEPs
    print("# UF: " + uf)
    pagini = 1
    while pagini<1100: #Percorrer todas as páginas de cada UF até não encontrar nenhum item novo.
        new = 0
        pagfin=pagini+99    #Definir os intervalos das páginas
        data = "UF="+str(uf)+"&pagini="+str(pagini)+"&pagfim="+str(pagfin)  #Enviar parametros para o site com informação da UF e inicio/fim da página
        resp = requests.post(url, headers=headers, data=data)
        soup = BeautifulSoup(resp.text, 'html.parser')
        tables = soup.find_all("table", { "class" : "tmptabela" })
        for table in tables:   #Percorrer a tabela buscando os valores desejados
            tabledata= table.find_all ("tr")
            for tr in tabledata:
                tddata = tr.find_all("td")
                if len(tddata)==4:
                    localidade = {
                        "Localidade": tddata[0].text.strip(),
                        "Faixa de CEP": tddata[1].text.strip(),
                        "ID": uf+str(idlocalidade)  #ID sendo gerada com a UF + um número em sequencia
                    }
                    skip = False
                    for board_member in board_members:  #Remoção de valores duplicados
                        if board_member["Localidade"] == localidade["Localidade"]:
                            skip = True
                            break
                    if not skip:
                        board_members.append(localidade)
                        idlocalidade +=1
                        new += 1
        pagini += 100
        print("\tNew = " + str(new) + "\n\tpagini: " + str(pagini))
        if new == 0:    #Validação para verificar existe algum item novo
            break 

def save_json(): #Exportar jsonl
    stringfile = ""
    for line in board_members:
        stringfile = stringfile + json.dumps(line,ensure_ascii=False) + "\n"
    with open("ufs.jsonl", "w") as fp:
        fp.write(stringfile)

for uf in consulta_uf(headers):
    consulta_cep(uf,idlocalidade)
save_json()
