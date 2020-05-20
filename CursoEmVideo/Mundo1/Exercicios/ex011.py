#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
lar = float(input('Qual a largura da sua parede: '))
alt = float(input('Qual a altura da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {}X{} e sua área é de {} m².'.format(lar, alt, area)) #atalho para o m² = CTRL+ALT+2
print('Para pintar essa parede, voce precisará de {} litros de tinta.'.format(area/2))