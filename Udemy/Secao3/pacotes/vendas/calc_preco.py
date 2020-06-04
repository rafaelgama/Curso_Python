
from vendas.formata import preco

def aumento(valor, porc, formata=False):
    r = valor + (valor * (porc /100))
    if formata:
        return preco.real(r)
    else:
        return r

def reducao(valor, porc, formata=False):
    r = valor - (valor * (porc /100))
    if formata:
        return preco.real(r)
    else:
        return r
    