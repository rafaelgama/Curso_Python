# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] # utilizando o processo de fatiamento de string.
while sexo not in 'MF':
    sexo = str(input('Sexo {} inválido, digite o sexo [M/F]: '.format(sexo))).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
print(cores['bvermelho']+'FIM!'+cores['limpa'])


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)