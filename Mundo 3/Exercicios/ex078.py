# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

num = []
maior = menor = 0
for c in range(0,5):
    num.append(int(input(f'Digite um Valor para a Posição {c}: ')) )
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]           
        if num[c] < menor:
            menor = num[c]
        
print(f'Você digitou os valores {num}.')
print(f'O maior valor digitado foi {maior}, na posição: ', end ='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {menor}, na posição: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')

print('')

print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)