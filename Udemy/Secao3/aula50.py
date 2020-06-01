# Funções (def) em Python - *args **kwargs - 

# or agumentos passados para um função, sempre são tratados em Tuplas().

def func(*args):
    print(args)
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

lista = [1,2,3,4,5,6]
func(lista) 
print('-='*30)
# coloca o * antes de enviar para desempacotar a lista para 
# funções que tem muiltiplos parametros.
func(*lista) 

print('-='*30)

# utilizando **kwargs- ele Cria um dicionário no segundo argumento.
def func2(*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    print(nome)

lista = [4,5,6,8,9]
func2(*lista, nome='Rafael',sobrenome='Gama') 
