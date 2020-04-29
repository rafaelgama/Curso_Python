#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. 
#Veja como utilizar o código \033[m com todas as suas principais possibilidades.
# Para iniciar a impressão da formatação = \033["Style";"Text";"Background"m
# Sempre abrir com "\033[" e  fechar sempre com "m" no final 
# Caso não seja preenchido nada, ele mantem e força o padrão = \033[m 
print('Olá Mundo humanos') #impressão padrão sem formatação
print('\033[1;31;43mOlá Mundo humanos') #impressão considerando a linha toda do temrinal

#impressão considerando somente as palavras digitadas, repetindo o comando no final para garantir que volte ao padrão quando termina a impressão.
print('\033[1;31;43mOlá Mundo humanos\033[m') 

print('\033[0;30;41mOlá Mundo humanos\033[m') #imprimindo uma cor para fazer o inverso na proxima linha.
print('\033[7;30;41mOlá Mundo humanos\033[m') #utilizando o 7, ele inverte as cores que vc digitou, como foi feito na linha acima.

#imprimindo duas cores na mesma linha:
a = 3
b = 5
print('O valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a,b))
#Fazendo a impressão dentro do format:
nome = 'Rafael'
print('O nome digitado foi: {}{}{}'.format( '\033[4;34m' ,nome, '\033[m' ))
#usando dicionário(array) para usar as cores:
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'pretoebranco':'\033[7:30m'}
print('O nome digitado foi: {}{}{}'.format( cores['amarelo'] ,nome, cores['limpa'] ))
print('O nome digitado foi: {}{}{}'.format( cores['pretoebranco'] ,nome, cores['limpa'] ))