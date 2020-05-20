# definição das funções.

def aumentar(preco=0, taxa=0, picture=False):
    res = preco + (preco * taxa/100)
    return res if picture is False else moeda(res)


def diminuir(preco=0, taxa=0, picture=False):
    res = preco - (preco * taxa/100)
    return res if picture is False else moeda(res)


def dobro(preco=0, picture=False):
    res = preco*2
    return res if picture is False else moeda(res)
 

def metade(preco=0, picture=False): 
    res = preco/2
    return res if picture is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')







