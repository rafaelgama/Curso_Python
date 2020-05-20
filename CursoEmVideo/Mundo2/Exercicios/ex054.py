#Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime # ou utilizar o formato: from datetime importe date
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

atual = datetime.date.today().year 
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
    else:
        print('Ano inválido, verifique!')
if maior > 0:
    print('Temos {} pessoas maiores de idade.'.format(maior))
if menor > 0:
    print('Temos {} pessoas menores de idade.'.format(menor))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)
