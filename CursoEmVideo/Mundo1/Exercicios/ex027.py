#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo é: {}'.format(nome))
nspl = nome.split()
print('Seu primeiro nome é: {}'.format( nspl[0] )) #em uma lista, quando digita 0,1,2,10... a leitura vai da esqueda pra direita
print('Seu último nome é: {}'.format( nspl[-1] ))  #em uma lista, quando digita -1,-2,-10... a leitura vai da direita pra esqueda
# outra forma de utilizar a ultima posição
print('Seu último nome é: {}'.format( nspl[len(nspl)-1] ))