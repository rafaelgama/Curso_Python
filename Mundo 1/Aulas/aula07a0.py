nome = input('Qual o seu nome ?')
#print normal
print('Prazer em conhece-lo {}!'.format(nome))
#print alinhado a ESQUERDA obervando que a varialvel tem tamanho de 20 caracteres
print('Prazer em conhece-lo {:<20}!'.format(nome))
#print alinhado a DIREITA obervando que a varialvel tem tamanho de 20 caracteres
print('Prazer em conhece-lo {:>20}!'.format(nome))
#print alinhado a CENTRALIZADO obervando que a varialvel tem tamanho de 20 caracteres
print('Prazer em conhece-lo {:^20}!'.format(nome))
#print CENTRALIZADO e preenchendo espacos com outro caractere
print('Prazer em conhece-lo {:#^20}!'.format(nome))