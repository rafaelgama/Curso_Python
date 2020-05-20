#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

totidade = 0
maioridahom = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print('-----{}° ---pessoa'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    totidade += idade
    if c == 1 and sexo == 'M':
        maioridahom = idade
        nomevelho = nome
    if idade > maioridahom and sexo == 'M':
        maioridahom = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    
print('A idade média do grupo é de {:.1f} anos.'.format(totidade/4))
print('O nome do homem mais velho é: {}, com {} anos.'.format(maioridahom,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)