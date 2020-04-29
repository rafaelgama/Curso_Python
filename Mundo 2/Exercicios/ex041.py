#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

anonas = int(input('Atleta, digite seu ano de nascimento: '))
anoatu = date.today().year
idade = anoatu - anonas

if idade <= 9:
    print('com a idade de {} anos, sua categoria é a MIRIM'.format(idade))
elif idade <= 14:
    print('com a idade de {} anos, sua categoria é a INFANTIL'.format(idade))
elif idade <= 19:
    print('com a idade de {} anos, sua categoria é a JÚNIOR'.format(idade))
elif idade <= 25:
    print('com a idade de {} anos, sua categoria é a SÊNIOR'.format(idade))
else:
    print('com a idade de {} anos, sua categoria é a MASTER'.format(idade))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)