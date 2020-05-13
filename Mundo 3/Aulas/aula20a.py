# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. 
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

# Empacotar parâmetros significa que quando vc não sabe quantos parâmetros receber, vc recebe tudo em um só.
# Exemplo 1 : 
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

 # chaamada da função contador()
contador(1, 2, 4)
contador(3, 5, 9, 8)
contador(2, 5)

# Exemplo 2 :
def soma(* val):
    s = 0
    for num in val:
        s += num
    print(f'A soma dos valores {val} é igual a {s}.')

# chaamada da função soma()
soma(2,4,5)
soma(4,8)

# Criando funções com chamadas de lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 6, 4, 7, 9]
dobra(valores) # chaamada da função dobra()
print(valores)