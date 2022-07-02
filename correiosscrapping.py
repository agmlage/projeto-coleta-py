import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

url = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "UF=SP"


resp = requests.post(url, headers=headers, data=data)

#print(resp.content)


#pagina = "<select name="UF" class="f1col"><option value="" <="" option=""></option><option value="AC">AC</option><option value="AL">AL</option><option value="AM">AM</option><option value="AP">AP</option><option value="BA">BA</option><option value="CE">CE</option><option value="DF">DF</option><option value="ES">ES</option><option value="GO">GO</option><option value="MA">MA</option><option value="MG">MG</option><option value="MS">MS</option><option value="MT">MT</option><option value="PA">PA</option><option value="PB">PB</option><option value="PE">PE</option><option value="PI">PI</option><option value="PR">PR</option><option value="RJ">RJ</option><option value="RN">RN</option><option value="RO">RO</option><option value="RR">RR</option><option value="RS">RS</option><option value="SC">SC</option><option value="SE">SE</option><option value="SP">SP</option><option value="TO">TO</option></select>"
#print (pagina.content)

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