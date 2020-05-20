#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3 
r = n ** (1/2)
p = pow(n,(1/2))
print('O dobro de {} é: {}'.format(n, d))
print('O triplo de {} é: {}'.format(n, t))
print('A raiz quadrada de {} é: {:.2f}'.format(n, r)) #{:.2f} siginifica que so imprime 2 casas decimis para ponto flutuante.
print('A raiz quadrada (pow) de {} é: {:.3f}'.format(n, p)) #{:.3f} siginifica que so imprime 3 casas decimis para ponto flutuante.