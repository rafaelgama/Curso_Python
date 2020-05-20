#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

r1 = float(input(cores['limpa']+'Primeira reta:'+cores['roxo']+' '))
r2 = float(input(cores['limpa']+'Segunda reta:'+cores['roxo']+' '))
r3 = float(input(cores['limpa']+'Terceira reta:'+cores['roxo']+' '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(cores['roxo']+'As retas podem formar um TRIANGULO '+cores['limpa'], end='') # Remove o enter no final da linha " end='' ".
    if r1 == r2 == r3:
        print(cores['bvermelho']+'EQUILÁTERO!'+cores['limpa'])
    elif r1 != r2 != r3 != r1: 
        print(cores['bvermelho']+'ESCALENO!'+cores['limpa'])
    else:
        print(cores['bvermelho']+'ISÓSCELES!'+cores['limpa'])
else:
    print(cores['vermelho']+'As retas NÂO podem formar um TRIANGULO'+cores['limpa'])

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)
