#Context Manager - Criando e usando gerenciadores de contexto.


arq = 'D:\\GitHub\\Curso_Python\\Udemy\\Secao4\\aula110\\abc.txt'

# A forma mais comum de abrir e fechar aquivos texto
'''file = open(arq, 'w')
file.write('Alguma coisa')
file.close()'''

# Outra forma de manipular arquivos
"""
with open(arq, 'w') as file:
    file.write('Alguma coisa de novo')
"""
#Usando o Gerenciador de contexto
from contextlib import contextmanager

@contextmanager # so funciona se chamar com o with
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir(arq, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')





