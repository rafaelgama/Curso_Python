# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# função para calcular a area:
def area(l, c):
    r = l * c
    print(f'A área de um terreno de {l}x{c} é de {r}m²')


print(f'{"Controle de terrenos":=^30}')
l = float(input('LARGURA: (m)'))
c = float(input('COMPRIMENTO: (m)'))
# chamada da função area()
area(l,c)


print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)