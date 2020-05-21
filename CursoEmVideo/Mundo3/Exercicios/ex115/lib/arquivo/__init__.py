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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','') 
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')      
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do Arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()








