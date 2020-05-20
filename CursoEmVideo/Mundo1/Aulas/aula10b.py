#Como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
nome = str(input("Qual o seu nome? ")).strip()
#Quando só se tem uma condição, é uma condição SIMPLES, se houver mais de uma será COMPOSTA.
if nome == 'Rafael':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format( nome ))