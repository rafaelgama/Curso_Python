
#https://docs.python.org/3/library/functions.html#open

# Criando, lendo, escrevendo e apagando arquivos.

import json
import os # para poder apagar o arquivo

print(f'{" ARQUIVOS-JSON":=^40}')
print('-=-'* 20)

arq = 'D:\\GitHub\\Curso_Python\\Udemy\\Secao3\\json.txt'

d1 = {
    'Pessoa 1':{
        'nome': 'Rafael',
        'idade': 40,
    },
       'Pessoa 2':{
        'nome': 'Gama',
        'idade': 35,
    },
}

# Transforma em arquivo json 
d1_json = json.dumps(d1,indent=True)

with open(arq, 'w+') as file:
    file.write(d1_json)

print(d1_json)

print(f'{" LEITURA-JSON":=^40}')
print('-=-'* 20)

with open(arq, 'r') as file:
    d1_ler = file.read()
    print(d1_ler)
    # Tranformar em dicionarios novamente
    d1_ler = json.loads(d1_ler)
    print()
    print(d1_ler)
    print()

for k, v in d1_ler.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)


os.remove(arq) # apagando o arquivo.
print('-=-'* 20)