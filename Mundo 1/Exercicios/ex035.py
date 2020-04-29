#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'roxo':'\033[35m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

r1 = float(input(cores['limpa']+'Primeira reta:'+cores['azul']+' '))
r2 = float(input(cores['limpa']+'Segunda reta:'+cores['azul']+' '))
r3 = float(input(cores['limpa']+'Terceira reta:'+cores['azul']+' '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(cores['roxo']+'As retas podem formar um TRIANGULO'+cores['limpa'])
else:
    print(cores['vermelho']+'As retas NÂO podem formar um TRIANGULO'+cores['limpa'])


print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)