# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais. 

# Lista são declaradas com colchetes [], diferente de tuplas que são parênteses ().
# A Diferença de listas e tuplas, são que listas são mutáveis e tuplas não.
# Exemplos
num = [1,3,4,6]
print(num)
num[2] = 9 # alterar o elemento pelo índice.
print(num)
num.append(7) # adiciona um elemento sempre no final da lista.
print(num)
num.sort() # Coloca em Ordem Crescente
print(num)
num.sort(reverse=True) # Coloca em Ordem Decrescente
print(num)
num.insert(0,4) # Insere um valor, indicando a posição, automaticamente ele reorganiza os índices da lista.
print(num)
num.pop() # Remove um elemeto da lista pelo indice, caso não indique alguma, o default é sempre o último.
print(num)
num.remove(3) #Remove o primeiro valor, ao invés do índice, encontrado na lista, caso não exista ele retorna um erro de programa.
print(num)

# outro exemplo de geração de listas
valores = []
'''valores.append(9)
valores.append(4)
valores.append(5)''' # Exemplo de como adicionar
# exemplo digitando os valores em listas.
#for i in range(0,5):
#    valores.append(int(input('Digite um valor: ')))

for i, v in enumerate(valores):
    print(f'Na posição {i}, encontrei o valor {v}!')
print('cheguei ao final da lista!')


# Exemplo de copias de listas
a = [1,3,5,7]
b = a # nesse exemplo, é feito apenas uma refença da lista a na b, e não uma cópia.
b[2] = 9
print(f'lista a {a}')
print(f'Lista b {b}')

c = [1,3,5,7]
d = c[:] # nesse exemplo, é feito uma cópia, ele percorre da primeira posição até a ultima da lista, gerando outro registro na memória.
d[2] = 9
print(f'lista c {c}')
print(f'Lista d {d}')
