#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' PALINDROMO ')) # centraliza(^) o texto no meio do caracteres de '='

frase = str(input('Digite uma frase: ')).strip().upper().split() #usando o split para separar as palavras pelo espaço
junto = ''.join(frase) # utiliza o aspas antes do .join() para juntar as palavras sem adcionar nada, nem espaço
tam = len(junto)-1
inverso = ''
for c in range(tam, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}.'.format(junto,inverso))
# outra solução sem utilizar o FOR e utilizando o fatiamento
#inverso = junto[::-1]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Essa frase não é um PALÍNDROMO!')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)