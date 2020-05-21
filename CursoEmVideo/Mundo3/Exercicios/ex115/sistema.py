
from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

thisdir = os.getcwd() # busca o diretório raiz do projeto

#print(thisdir)

arq = thisdir+'\Mundo3\Exercicios\ex115\cursoemvideo.txt'

if not arqExiste(arq):    
    criarArq(arq)
    #print('Arquivo não encontrado!')

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArq(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema. Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção Válida!\033[m')
    sleep(1)







