#Ler a largura e altura da parede e calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que 1l = 2m quadrado
nA = float(input('Qual a altura da parede?'))
nL = float(input('Qual a largura da parede?'))
a = nA * nL
print('A parede com {} metros de altura e {} metros de largura, tem {} metros quadrados '.format(nA, nL, a))
print('Se 1 litro de tinta pode pintar 2m quadrados, será necessário de {} litros de tinta para essa parede.'.format(a/2))


