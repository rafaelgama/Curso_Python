#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('='*10)
print('\033[7;30m_INICIO_\033[m')
print('='*10)

num = int(input('Digite um número, para eu dizer se é PAR ou IMPAR: '))
res = num % 2
if res > 0:
    print('O número digitado {} é \033[;36mIMPAR\033[m'.format(num))
else:
    print('O número digitado {} é \033[;33mPAR\033[m'.format(num))

print('='*10)
print('\033[7;30m___FIM___\033[m')
print('='*10)