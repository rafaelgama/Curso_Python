#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

fim = 'S'
med = soma = menor = maior = qtd = 0
while fim not in 'Nn':
    num = int(input('Digite um número: '))
    soma += num    
    if menor > num or menor == 0 :
        menor = num
    if maior < num or maior == 0:
        maior = num
    qtd += 1
    fim = str(input('Deseja Continuar [S/N]? '))
med = soma/qtd
print('Voce digitou {} numeros e a média foi {:.2f}.'.format(qtd,med))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)