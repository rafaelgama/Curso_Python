# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# definição da função
def leiaInt(var):
    ok = False
    valor = 0
    while True: 
        num = str(input(var))
        if num.isnumeric():
            num = int(num)
            ok = True
        else:
            print(cores['bvermelho']+'ERRO! Digite um número inteiro válido!'+cores['limpa'])
        if ok:
            break
    return num

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}.')

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)