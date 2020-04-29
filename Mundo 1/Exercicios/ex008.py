#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite um valor de medida em metros: "))
dam = m /10
hm = m /100
km = m /1000
dm = m *10
cm = m *100
mm = m *1000
print('O valor de {} metro(s) são {} decâmetro(s)!'.format(m, dam))
print('O valor de {} metro(s) são {} hectômetro(s)!'.format(m, hm))
print('O valor de {} metro(s) são {} Quilômetro(s)!'.format(m, km))
print('O valor de {} metro(s) são {:.0f} Decímetro(s)!'.format(m, dm))
print('O valor de {} metro(s) são {:.0f} Centímetro(s)'.format(m, cm))
print('O valor de {} metro(s) são {:.0f} Milímetro(s)!'.format(m, mm))