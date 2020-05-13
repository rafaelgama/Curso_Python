# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, 
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, 
# escopo de variáveis e retorno de resultados. 

print(f'{"Parâmetros Opcionais":=^40}')
# Parâmetros Opcionais
# para que não tenha erros na quantidade de parametros recebidos, voce pode inicializar eles na passagem da chamada da função.
# Exemplo com a função somar()
def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A Soma vale {s}.')

#chamad da função
somar(2,3,4)
somar(2,8)
somar(b=3,a=5)

print(f'{"Utilizando o RETURN":=^40}')
# utilizando o retorno de resultado.
# Exemplo com a função somar()
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

#chamad da função
r1 = somar(3,5,7)
r2 = somar(9,2)
r3 = somar(b=4,a=7)

print(f'A Soma dos valores são {r1}, {r2}  e {r3}.')