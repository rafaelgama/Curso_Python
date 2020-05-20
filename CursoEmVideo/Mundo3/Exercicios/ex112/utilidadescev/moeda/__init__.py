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


def resumo(preco=0, taxaa=10, taxad=5):
    print('-=' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-=' *30)
    print(f'Preço analisado: \t{moeda(preco)}')  # \t = imprime tabulado
    print(f'Ddobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumemnto: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(preco, taxad, True)}')
    print('-=' *30)
    



