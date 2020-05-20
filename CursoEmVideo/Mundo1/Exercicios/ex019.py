#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = input("Qual o nome do 1o aluno: ")
a2 = input("Qual o nome do 2o aluno: ")
a3 = input('Qual o nome do 3o aluno: ')
a4 = input('Qual o nome do 4o aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))