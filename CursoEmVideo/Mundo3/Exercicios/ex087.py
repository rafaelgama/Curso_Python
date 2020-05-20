# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

matriz = [[0,0,0], [0,0,0], [0,0,0]] # preehce com zeros para não precisar utilizar append
for l in  range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um Valor para [{l},{c}]: '))
print('-^-'*10)
par = tercol = maior = 0    
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            tercol += matriz[l][c]
        if l == 1 and matriz[l][c] > maior or maior == 0:
            maior = matriz[l][c]
    print()
print(f'A soma dos valores Pares são: {par}.')
print(f'A soma da terceira coluna é igual a {tercol}.')
print(f'O maior valor da segunda é igual a {maior}.')

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)