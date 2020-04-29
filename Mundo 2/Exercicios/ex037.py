#screva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
cores =  {'limpa':'\033[m',
            'bazulm':'\033[1;36m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'__INICIO__'+cores['limpa'])
print('-=-'*10)

num = int(input('Digite um número inteiro: '))
print('Escolha uma opção para a conversão: ')
print('[ 1 ] converter para Binario')
print('[ 2 ] converter para Octal')
print('[ 3 ] converter para Hexadecimal')
opcao = int(input('Qual sua Opção? '))

if opcao == 1:
    # A função bin() sempre retorna "0b" mais o resultado sem tratamento de caractere. ex: bin(num)
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:] )) #tratamento para tirar as duas primeiras casas do retorno da função.
elif opcao == 2:
    # A função oct() sempre retorna "0o" mais o resultado sem tratamento de caractere. ex: oct(num)
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:] )) #tratamento para tirar as duas primeiras casas do retorno da função.
elif opcao == 3:
    # A função hex() sempre retorna "0x" mais o resultado sem tratamento de caractere. ex: hex(num)
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num).strip('0x') )) #tratamento para tirar as duas primeiras casas do retorno da função.
else:
    print('{} não é uma opção válida, tente novamente!'.format(opcao))


print('-=-'*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('-=-'*10)