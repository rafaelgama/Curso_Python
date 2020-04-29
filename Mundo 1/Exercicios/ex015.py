#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos quilômetros foram percorridos: KM'))
dia = int(input('Quantos dias o carro está alugado: '))
vkm = km*0.15
vdia = dia*60
print('O valor a ser pago no aluguel do carro é de R${:.2f} reais.'.format(vkm+vdia))
