# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# chamada principal
import moeda

p = float(input('Digite um preço R$: '))
print(f'A metade de {p:.2f} é {moeda.metade(p):.2f}')
print(f'O dobro de {p:.2f} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo 10%, temos {moeda.diminuir(p, 10):.2f}')