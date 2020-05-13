# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

# def = definição de funções 
# exemplo de função simples.
def lin(): 
    print('-='*30)

lin()  # chaamada da função lin()
print('SISTEMA DE ALUNOS')
lin()  # chaamada da função lin()

# exemplo de função com parâmetro.
def lin2(msg):
    print('-='*30)
    print(msg)
    print('-='*30)

# chaamada da função lin2()
lin2("FUNÇÃO COM PARÂMETRO")

# exemplo de função com parâmetro alterando os valores nos parâmetros.
def soma(a,b):
    print(f'A = {a} e B = {b}.')
    s = a+b
    print(f'A som de A+B = {s}.')

# Chamada normal soma()
soma(5,7)
# Chamada alterando valores no parametro soma()
soma(b=3, a=8) #sempre que forçar o parâmetro, ou força tudo, eu não força nada.


