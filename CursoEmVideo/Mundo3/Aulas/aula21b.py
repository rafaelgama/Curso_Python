# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, 
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, 
# escopo de variáveis e retorno de resultados. 


print(f'{"Escopo de Variáveis":=^40}')
# Escopo de Variáveis
def teste(b):
    global p # declarando a variável como global para pode utilizar o mesmo valor dentro das funções.
    x = 8
    p = 5
    print(f'Na função teste n vale {n}.')
    print(f'Na função teste x vale {x}.')
    print(f'Na função teste p vale {p}.')


# Chamada da função - Programa Principal
n = 2
print(f'No programa principal n vale {n}.')
p = 3
teste(p)
print(f'No programa principal p vale {p}.')



 
