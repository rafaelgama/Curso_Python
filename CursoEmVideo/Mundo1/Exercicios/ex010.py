#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere o dolar 1.00US$ = R$3.27
din = float(input('Quantos reais (R$) você tem na carteira para comprar em dolar: '))
res = din /3.27
print('Você pode compra com R${:.2f} reais, U${:.2f} dolares!'.format(din, res))
