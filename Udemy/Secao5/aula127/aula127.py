"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

Lista de conversão De/Para =>
DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from dados import *
import json

# o metodo dumps() com o s no final, é para converter pra uma string
"""
lista = [1,2,3,4,5,6]
print(lista, type(lista))
dados_json = json.dumps(lista)
print(dados_json, type(dados_json))
"""
# Exemplo de conversão de dicionário em str Json, result. = objetc json
# indent=4, para fazer a string json imprimir de forma indentada com 4 espaços.
#dados_json = json.dumps(clientes_dicionario, indent=4)
#print(dados_json, type(dados_json))


# Exemplo de conversão de str Json para dicionario em python
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

# Exporta dicionário para arquivo JSON
with open('clientes.json', 'w') as f:
    # utiliza o dump() para converter em um arquivo sem o "s"
    json.dump(clientes_dicionario, f, indent=4)


# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as f:
    # para leitura de arquivo utiliza o load() sem o "s".
    data = json.load(f)

print('-=-' * 20)
print(data)