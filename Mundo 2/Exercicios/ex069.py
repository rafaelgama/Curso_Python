# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

maior18 = hom = mulher = 0
while True:
    print('-+'*10)
    print('CADASTRE UMA PESSOA')
    print('-+'*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-+'*10)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade <= 20:
        mulher += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break

print(f'Total de pessoas mais de 18 anos: {maior18}.')
print(f'Ao todo temos {hom} homens cadastrado.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)