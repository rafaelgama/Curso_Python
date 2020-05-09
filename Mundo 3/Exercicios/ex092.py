# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

dado = dict()
dado['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dado['idade'] = datetime.today().year - nasc
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dado['ctps'] != 0:
    dado['contratação'] = int(input('Ano de Contratação: '))
    dado['salário'] = float(input('Salário: R$'))
    dado['aposentadoria'] = dado['idade'] + ( (dado['contratação'] + 35) - datetime.today().year )

print(f'{"VALORES CALCULADOS":=^40}')
for k, v in dado.items():
    print(f'- {k} tem o valor {v}')




print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)