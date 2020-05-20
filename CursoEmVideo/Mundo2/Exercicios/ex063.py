#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' SEQUENCIA FIBONACCI '))

qtd = int(input('Quantos termos você quer motrar? '))
t1 = 0
t2 = 1
t3 = 0
cnt = 3
print('{} -> {}'.format(t1,t2), end='')
while cnt <= qtd:    
    t3 = t1+t2 
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cnt += 1
print(cores['roxo']+' - Fim'+cores['limpa'])

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)