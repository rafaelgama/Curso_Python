# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# dicionários simples
pessoas = {'nome':'Rafael', 'sexo':'M', 'idade':40 }
print(f'{"Print Normal":=^40}')
print(f" O {pessoas['nome']} tem {pessoas['idade']} anos")

print(f'{"Print com keys()":=^40}')
print(pessoas.keys())

print(f'{"Print com values()":=^40}')
print(pessoas.values())

print(f'{"Print com items()":=^40}')
print(pessoas.items())

print(f'{"Print com laços - keys()":=^40}')
for k in pessoas.keys():
    print(f'{k}')

print(f'{"Print com laços - values()":=^40}')
for v in pessoas.values():
    print(f'{v}')

print(f'{"Print com laços - items()":=^40}')
for k, v in pessoas.items():
    print(f'{k} = {v}')    

# Exemplo de como alterar um dicionario
print(f'{"Print com alterar um dicionario":=^40}')
pessoas['nome'] = 'Macedo'
print(pessoas.items())

# Exemplo de como deletar um dicionario
print(f'{"Print com deletar um dicionario":=^40}')
del pessoas['nome']
print(pessoas.items())

# Exemplo de como adicionar em um dicionario
print(f'{"Print com adicionar em um dicionario":=^40}')
pessoas['Peso'] = 85.5
print(pessoas.items())
