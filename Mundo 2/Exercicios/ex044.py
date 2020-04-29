#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

print('{:=^40}'.format(' LOJAS RAFAEL ')) # centraliza(^) o texto no meio do caracteres de '='

compra = float(input('Qual o preço das compras: R$ '))
print('Fomas de pagamento: \n[ 1 ] - à vista dinheiro/cheque \n[ 2 ] - à vista cartão \n[ 3 ] - até 2x no cartão \n[ 4 ] - 3x ou mais no cartão')
forpag = int(input('Qual a opção? '))

if forpag == 1:
    valfim = compra - (compra * 10 /100)
    print('Para opção 1, sua compra de R${:.2f} reais, custará R${:.2f} reais. 10% de desconto.'.format( compra, valfim ))
elif forpag == 2:
    valfim = compra - (compra * 5 /100)
    print('Para opção 2, sua compra de R${:.2f} reais, custará R${:.2f} reais. 5% de desconto.'.format( compra, valfim ))
elif forpag == 3:
    valfim = compra/2
    print('Para opção 3, sua compra parcelada de R${:.2f} reais, custará R${:.2f} reais cada parcela.'.format( compra, valfim ))
    
elif forpag == 4:
    parc = int(input('Quantas parcelas? '))
    if parc >= 3:
        valfim = (compra + (compra * 20 /100))/parc
        print('Para opção 4, sua compra parcelada de R${:.2f} reais, custará R${:.2f} reais cada parcela com juros de 20%.'.format( compra, valfim ))
    else: 
        print('Para opção 4 não pode haver menos que 3 parcelas, verifique!')
else:
    print('Opção Inválida ou inexistente, verifique!')    


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)