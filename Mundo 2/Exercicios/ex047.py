#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' NUMEROS PARES ')) # centraliza(^) o texto no meio do caracteres de '='
# foma de calculo padrão, utilizando o MODULO
for c in range(1,51):
    if c % 2 == 0:
        print(c, end=' ')  # end =' ' é o comando para remover o o ENTER no final do print
print(cores['bvermelho']+'FIM!'+cores['limpa'])

# foma de calculo padrão, utilizando utlizando o intervalo
for c in range(2,51, 2):
    print(c, end=' ')  # end =' ' é o comando para remover o o ENTER no final do print
print(cores['bvermelho']+'FIM!'+cores['limpa'])

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)