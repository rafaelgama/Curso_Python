#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o angulo que vc deseja: '))
seno = math.radians(ang)
cos = math.radians(ang)
tan = math.radians(ang)
print('O Ângulo de {} tem o SENO de {:.2f}'.format(ang, math.sin(seno) ))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(ang, math.cos(cos) ))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, math.tan(tan)))
