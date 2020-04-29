#aça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05 # ou preco *(5/100)
print('Um produto com o valor de R${:.2f} reias, \nAplicando 5% desconto vai custar R${:.2f} reais.'.format(preco, preco-desconto))