#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip() #Pode-se eliminar os espaços na hora da digitação
#nome = 'Rafael Gama de Macedo Junior'
print('Tudo em letras maiúsculas: {}'.format(nome.upper()))
print('Tudo em letras minúsculas: {}'.format(nome.lower()))
print('Tudo em letras Capitais: {}'.format(nome.capitalize()))
print('Tudo em letras Titulos: {}'.format(nome.title()))
print('Quantas letras existem sem espaços: {}'.format(len(nome.strip()) - nome.count(' ') )) #tira todos os espços em branco na contagem.
listado = nome.split()
print('Quantas letras existem no primeiro nome: {}'.format(len(listado[0])) ) #quantas letras tem o primeiro nome
#ou pode imprimnir até encontrar o espaço em branco
print('Quantas letras existem no primeiro nome: {}'.format( nome.find(' ') ))