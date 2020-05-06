# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em 
# uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

numero = [[], []]
valor = 0
for n in range(1,8):
    valor = int(input(f'Digite um valor na {n}º posição: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

numero[0].sort()
numero[1].sort()
print(f'Os Valores Pares são: {numero[0]}.')
print(f'Os Valores Ímpares são: {numero[1]}.')


print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)