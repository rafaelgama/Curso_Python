#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if maior < peso or maior == 0:
        maior = peso
    if menor > peso or menor == 0:
        menor = peso
print('O menor peso são {:.1f}kg e o maior peso são {:.1f}kg.'.format(menor, maior))


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)