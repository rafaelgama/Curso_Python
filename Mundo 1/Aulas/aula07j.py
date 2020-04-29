#Algoritimo que leia o salario do funcionario e mostre seu novo salario, com 15% de aumento
n = float(input('Qual o valor do seu salário? '))
d = (n*15)/100
print('O seu salário com valor de {} reais, com 15% de aumento fica por: {} reais.'.format(n, n+d))
