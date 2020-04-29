n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#para não quebrar a linha de um print para o outro -> end=''
print('A soma é {}, o produto é {} e a divisão é {:.3f} '.format(s, m, d) , end=' ') 
print('A divisão inteira é {} e a potência é {}'.format(di, e))
#para quebrar a linha em qualquer ponto --> \n
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f} '.format(s, m, d) )
#para não quebrar a linha de um print para o outro -> end='>>> '
print('A soma é {}, o produto é {} e a divisão é {:.3f} '.format(s, m, d) , end='>>> ') 
print('A divisão inteira é {} e a potência é {}'.format(di, e))
