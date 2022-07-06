# Desafio Técnico - Busca CEP


## Descrição
Projeto para coleta e raspagem no site dos [correios](https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm) a fim de trazer as informações dos CEPs de todos os estados.
Neste projeto foi utilizada a linguagem Python e algumas bibliotecas para que fosse possível realizar a coleta dos dados refente aos estados brasileiros e suas respectivas cidades.

Para que fosse possível a coleta dos dados foram utilizadas as bibliotecas listadas abaixo.

### Bibliotecas Utilizadas

- wsgiref.headers
```
from wsgiref import headers
```
[Doc](https://docs.python.org/pt-br/3.8/library/wsgiref.html?highlight=headers#module-wsgiref.headers)
Utilizado para trabalhar com o cabeçalho do site, conseguinto utilizar as informações das UFs e avançar nas páginas.

- Requests
```
pip install requests
import requests
```
[Doc](https://requests.readthedocs.io/en/latest/)
Utilizado para enviar solicitações ao site a fim de retornar as informações desejadas
- CaseInsensitiveDict
```
from requests.structures import CaseInsensitiveDict
```
Dicionário utilizado no cabeçalho do site

- BeautifulSoup
```
pip install bs4
from bs4 import BeautifulSoup
```
[Doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Biblioteca utilizada para extrair dados de arquivos HTML e XML.
- Json
```
pip install json
import json
```
[Doc](https://docs.python.org/3/library/json.html)
Biblioteca usada para exportar os arquivos
