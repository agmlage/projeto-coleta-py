# Desafio Técnico - Busca CEP


## Descrição
Projeto realizado a fim de obter dados de todos os CEPs nacionais por meio da coleta e raspagem no site dos [Correios](https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm). 

Neste projeto, além da linguagem Python, foram utilizadas algumas bibliotecas que possibilitaram a coleta dos dados referentes aos estados brasileiros e suas respectivas cidades.
Para a execução deste, uma varredura foi realizada no site, seguida da exportação das informações relacionadas a Localidade e Faixa do CEP. Além disso, foram gerados IDs com a informação da Unidade Federativa concatenado a um índice incremental para cada localidade.

## Execução

```python
python Scraping.py
```

### Bibliotecas Utilizadas

- wsgiref.headers
```python
from wsgiref import headers
```
[Doc](https://docs.python.org/pt-br/3.8/library/wsgiref.html?highlight=headers#module-wsgiref.headers)
Utilizado para trabalhar com o cabeçalho do site, permitindo o uso das informações das UFs e o avanço nas páginas.

- Requests
```python
pip install requests
import requests
```
[Doc](https://requests.readthedocs.io/en/latest/)
Utilizado para requisitar ao site as informações desejadas.
- CaseInsensitiveDict
```python
from requests.structures import CaseInsensitiveDict
```
Dicionário utilizado no cabeçalho do site.

- BeautifulSoup
```python
pip install bs4
from bs4 import BeautifulSoup
```
[Doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Utilizado para extrair dados de arquivos HTML e XML.
- Json
```python
pip install json
import json
```
[Doc](https://docs.python.org/3/library/json.html)
Utilizado para exportar os arquivos.
