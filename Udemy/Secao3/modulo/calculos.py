# utilização de modulos em Python.

import math

print('-=-'* 20)
print(f'{" MODULOS-calculos ":=^40}')


PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

# caso precise garantir que só quando for __main__ coloque um IF:
if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

# __main__ sempre é o primeiro fonte chamado.
print(__name__)

# caso precise garantir que só quando for __main__ coloque um IF:
# if __name__ == '__main__':

print('-=-'* 20)