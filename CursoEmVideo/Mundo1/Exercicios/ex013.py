#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
valnovo = salario+(salario * 15/100) #ou 0.15
print('Um funcionário que recebe R${:.2f} reais de salário,\ncom 15% de aumento vai receber R${:.2f} reais'.format(salario, valnovo))
