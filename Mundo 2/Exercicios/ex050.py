#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 
soma = 0
count = 0
for c in range(0,6):
    num = int(input('Digite um número inteiro:'))
    if  num % 2 == 0:
        soma += num
        count += 1
print('A soma de {} numeros pares são: {}'.format(count,soma))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)