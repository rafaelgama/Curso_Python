# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# função para calcular fatorial()
def fatorial(n, show=False):
    """[summary]

    Arguments:
        n {int} -- O número a ser calculado

    Keyword Arguments:
        show {bool} -- Se deverá mostrar ou não a conta (default: {False})

    Returns:
        [int] -- O Valor fatorial de um número n.
    """
    lisret = list()
    calc = n
    fator = 1
    print(f'Calculando o Fatorial de {n}! = ', end='')
    while calc > 0:
        if show:
            print(f'{calc}',end = '')
            print(' X ' if calc > 1 else ' = ' , end='')
        fator = fator*calc
        calc -= 1
    return fator

# Chamada principal
num = int(input('Digite um número para calcular o Fatorial: '))
print(fatorial(num,True))
help(fatorial)

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)