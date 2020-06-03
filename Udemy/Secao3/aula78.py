# https://docs.python.org/3/library/exceptions.html

# Levantando exceções em Python

print('-=-'* 20)

print(f'{" Exemplo com o raise ":=^40}')

def divide(n1,n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1 / n2

# para capturar a exceção
try:
    print(divide(2,0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print('Log:',error)

print('-=-'* 20)