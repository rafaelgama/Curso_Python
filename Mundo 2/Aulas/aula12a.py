#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
# exemplos
nome = str(input('Qual é o seu nome? ')).strip()
 
if nome == 'Rafael':
    print('Que nome bonito!!')
elif nome == 'Pedro ' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Juliana Jessica':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum.')
print('Tenha um ótimo dia {}.!'.format(nome))