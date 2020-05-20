#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'roxo':'\033[35m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

valres = float(input('Qual o valor da residencia a venda? '))
salario = float(input('Qual o valor do salário do comprador? '))
anos = int(input('Em quantos anos vc pretende pagar? '))

valpres = valres/anos*12
sal30 = salario * 30/100

if valpres > sal30:
    print('O valor da prestação é de R${:.2f} reais e ultrapassa o limite de R${:.2f} reais (30%).'.format(valpres,sal30))
    print(cores['vermelho']+'Financiamento NEGADO!'+cores['limpa'])
else:
    print('O valor da prestação é de R${:.2f} reais e está no limite de R${:.2f} reais (30%).'.format(valpres,sal30))
    print(cores['azul']+'Financiamento APROVADO!'+cores['limpa'])
    
print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)