#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A primeira nota foi {:.1f} e a segunda foi {:.1f} e a sua média é: {:.1f}'.format(n1, n2, m))