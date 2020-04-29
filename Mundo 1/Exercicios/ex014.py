#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
grau = float(input('Digite a temperatura em °C: '))  #atalho para o simbolo de grau = ALT+0176
farn = (grau *1.8) + 32
print('A temperatura de {} °C, equivale a {} °F'.format(grau, farn))
