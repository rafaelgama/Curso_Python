# funções Decoradoras e decoradores.
"""
Uma função decoradora é uma função que aceita outra função como argumento (a função decorada), 
realiza algum processamento com a função decorada e a devolve ou a substitui por outra função 
que poderá ser invocada posteriormente.
"""
from time import sleep

def velo(func):
    print('velo')
    return func

@velo
def demo():
    for i in range(5):
        print(i)
        sleep(0.5)

demo()

