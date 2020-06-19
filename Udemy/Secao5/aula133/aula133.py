# Sys.argv - Executando arquivos com argumentos no sistema.
# Exemplo de como executar programas via terminal, passando parâmetros
# ex: (venv) D:\GitHub\Curso_Python\Udemy\Secao5\aula133>python aula133.py -a -d
import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos')
    print('-a', 'Para listar todos os arquivos neste pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios neste pasta', sep='\t')

    # para matar a execução do programa no terminal
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        # verifica se existem arquivos no diretorio
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        # verifica se existem diretorios no diretorio
        if os.path.isdir(arquivo):
            print(arquivo)



#print(argumentos)

