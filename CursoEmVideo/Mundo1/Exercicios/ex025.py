#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Qual seu nome completo: ")).strip() #Remove os espaços em branco na digitação.
#Essa resolução não trata nomes tipo silvana ou algo do tipo.
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper() ))

#essa solução pega somente o nome "Silva"
name = str(input('Digite um nome: ')).title()
name = '{} '.format(name)
teste = str(name.count('Silva ') > 0)
teste = teste.replace('False', 'não tem')
teste = teste.replace('True', 'tem')
aspas = '"'
name = name.strip()
print('{} {} {}Silva{} no nome'.format(name, teste, aspas, aspas))