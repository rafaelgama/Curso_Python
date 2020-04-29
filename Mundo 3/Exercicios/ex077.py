# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

palavras = ('APRENDER','PROGRAMAR','LER','SABEDORIA','PYTHON','CURSO','GRATIS','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for c in range(0,len(palavras)):
        
    print(f'\nNa palavra {palavras[c]} temos', end ='')
    for vog in range(0,len(palavras[c])):
        if palavras[c][vog] in 'AEIOU':
            print(f' {palavras[c][vog]}', end='')

print('')

print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)