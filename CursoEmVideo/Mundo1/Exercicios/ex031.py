#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

dist = float(input(cores['azul']+'Qual a distância da sua viajem? '+cores['limpa']))
print('Voce está prestes a começar uma viajem de {}{}{} km'.format( cores['amarelo'], dist, cores['limpa'] ))
if dist > 200:
    print('O preço da sua passagem será: {}R${:.2f}{} reais '.format(cores['vermelho'], dist*0.45, cores['limpa']))
else:
    print('O preço da sua passagem será: {}R${:.2f}{} reais '.format(cores['amarelo'], dist*0.50, cores['limpa']))

#modelo IN LINE da condicional
preco = dist*0.50 if dist <= 200 else dist*0.45
print('O preço IN LINE da sua passagem será: {}R${:.2f}{} reais '.format(cores['pretoebranco'], preco, cores['limpa']))

print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)
