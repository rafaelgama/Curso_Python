#fazer um algoritmo que leia um preco de produto e mostre  seu novo preco com 5% de desconto
n = float(input('Qual o preço do produto? '))
d = (n*5)/100
print('O produto com valor de {} reais, com 5% de desconto fica por: {} reais.'.format(n, n-d))

