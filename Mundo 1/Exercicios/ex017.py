#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
catop = float(input('Qual o comprimento do cateto oposto: '))
catad = float(input('Qual o comprimento do cateto adjacente: '))
hip = (catop ** 2 + catad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip)) 

#Usando o modulo math
'''import math
catop = float(input('Qual o comprimento do cateto oposto: '))
catad = float(input('Qual o comprimento do cateto adjacente: '))
hip = math.hypot(catop, catad)
print('A hipotenusa vai medir {:.2f}'.format(hip))'''