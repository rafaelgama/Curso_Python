# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

n = s = q =0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    print('{} '.format(n))
    if n == 999:
        break
    s += n
    q += 1
print(f'A foram digitados \033[35m{q}\033[m valores e a soma vale {cores["pretoebranco"]}{s}{cores["limpa"]}.')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)