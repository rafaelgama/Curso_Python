from lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')  # rt = reading text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, 'wt+') # wt+ siginifica que é pra criar um arquivo para writing text e o sinal de + é para criar o arquivo.
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquvo {nome} criado com sucesso')

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())

