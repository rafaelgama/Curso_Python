
from lib.interface import *
from time import sleep

#cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema. Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção Válida!\033[m')
    sleep(1)







