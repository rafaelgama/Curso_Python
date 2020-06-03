# Try e except como condicional

print('-=-'* 20)

print(f'{" Exemplo com condicional ":=^40}')

def conv_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    num = conv_num(input('Digite um número: '))

    if num is None:
        print('Erro: isso não é um número')
    else:
        print(num * 5)




