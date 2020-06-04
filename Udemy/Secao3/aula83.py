#https://docs.python.org/3/library/functions.html#open

# Criando, lendo, escrevendo e apagando arquivos.

import os # para poder apagar o arquivo

print(f'{" ARQUIVOS ":=^40}')
print('-=-'* 20)

arq = 'D:\\GitHub\\Curso_Python\\Udemy\\Secao3\\abc.txt'

file = open(arq, 'w+') # utilizando o w+ ele apaga se tiver algum conteúdo.
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# move o curso para a linha desejada
file.seek(0,0)

print('Lendo Linhas - read(): ')
print(file.read()) # le todo o arquivo


# move o curso para a linha desejada
file.seek(0,0)
print('Lendo Linhas - readline(): ')
print(file.readline(), end='') # le linha a linha o arquivo
print(file.readline(), end='')
print(file.readline(), end='')

print()
# move o curso para a linha desejada
file.seek(0,0)
print('Lendo Linhas - readlines(): ')
for linha in file.readlines():
    print(linha, end='')

file.close()

# Com o modo "with" ele gerencia o arquivo, não sendo necessário fechar.
print(f'{" ARQUIVOS - with ":=^40}')
print('-=-'* 20)

#  utilizando o a+ para não apagar o conteudo
with open(arq, 'a+') as file:
    file.write('Linha 4\n')
    file.write('Linha 5\n')
    file.seek(0)
    print(file.read())

os.remove(arq)

print('-=-'* 20)