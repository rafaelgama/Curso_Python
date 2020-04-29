#Como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a seegunda nota: '))
m = (n1+n2)/2
print('A média da nota é: {:.1f}'.format( m ))
if m >= 6:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, Estude mais!')
#Formato simplificado
print("Parabéns!" if m >= 6 else 'Estude mais!')