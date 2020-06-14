# CSV, Comma Separated Values

"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""

import csv

arq = r'D:\GitHub\Curso_Python\Udemy\Secao5\aula128'

with open(arq+'\contatos.csv', 'r') as arquivo:
    # carrega um objeto do tipo Iterador
    #dados = csv.reader(arquivo) # Le o arquivo e cada linha é uma lista
    #dados = csv.DictReader(arquivo) # Carrega as linhas para o formato de dicionário
    #next(dados)
    # Para converter os dados em uma lista/dict, para usar fora do gerador with.
    dados = [x for x in csv.DictReader(arquivo)]

    #for dado in dados:
    #    print(dado)
    ## imprime o resultado no formato de dicionario:
    #for dado in dados:
    #    print(dado['Nome'],dado['Sobrenome'])


# newline='' = remove os ENTERS das linhas na hora de gerar o arquivo
with open(arq+'\contatos2.csv', 'w', newline='') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    # Pegar somente as chaves dos dicionários
    chaves = dados[0].keys()
    chaves = list(chaves)
    # Grava o cabeçário do arquivo .csv
    escreve.writerow(
        [
        chaves[0],
        chaves[1],
        chaves[2],
        chaves[3],
        ]
    )
    # faz a leitura dos valores para a gravação
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']

            ]
        )
        








