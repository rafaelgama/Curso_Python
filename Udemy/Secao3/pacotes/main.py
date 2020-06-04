# Como criar pacotes e módulos em Python.

import vendas.calc_preco 
# ou from vendas.calc_preco impoort aumento, reducao 

print(f'{" PACOTES-main ":=^40}')
print('-=-'* 20)

preco = 49.90
preco_maior = vendas.calc_preco.aumento(preco, 15,True)
print(preco_maior)

preco_menor = vendas.calc_preco.reducao(preco, 15,True)
print(preco_menor)


print('-=-'* 20)