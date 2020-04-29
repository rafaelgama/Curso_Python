# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. 
# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, 
# acessíveis por chaves individuais.

# Tuplas são IMUTÁVEIS
# Tuplas podem ter dados de tipos diferentes na mesma Tupla.

lanche = ('Hambuguer','Suco','Pizza','Pudim')
print(lanche) # Imprime todos
print(lanche[0]) # Imprime a primeira casa, lembrando que sempre inicia com 0
print(lanche[3]) # Imprime  ultimo elemento, lembrando o ultimo elemento pode ser tb 0 -1. 
print(lanche[1:3]) # Imprime do primeiro numero até a penultima casa, a ultima sempre é ignorada.
print(lanche[2:]) # Imprime da posição 2 até o final. Quando não se define o ultimo elemente, ele imprime até o final.
print(lanche[:2]) # Imprime o primeiro elemento, quando não se define a posição, e vai até a posição definida -1. Nunca é impresso a ultima posição.

# utilizando FOR direto nas tuplas
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba')

# utilizando o FOR com o 'in range'.
for c in range(0,len(lanche)): # lembrando que o range sempre ignora o ultimo valor.
    print(f'Eu tb vou comer {lanche[c]}.')
print('Comi pra caramba de novo')

# utilizando o FOR com 'enumerate'.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba outra vez')

# Imprimir ordenado, mas não altera a Tupla, so ordena para impressão.
print(sorted(lanche))

# Concotenação de Tuplas, ele não altera os valores, mas concatena
a = ('1','5','3')
b = ('5','7','9','8')
c = a + b
print(c)
# verifica quantos caracteres tem na tupla.
print(c.count('5')) 
# retorna qual a posição que está o caracter na primeira ocorrencia
print(c.index('5')) 
# caso exista mais de uma, coloque no segundo parametro para iniciar a partir dele.
print(c.index('5',2)) 
# Pode deletar a tupla inteira, mesmo que existam tipos diferentes
del(a)
print(a)