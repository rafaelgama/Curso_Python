#Como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
tempo = int(input('Quantos anos tem o seu carro! '))
#exemplo pulando linha
if tempo <= 3:
    print('Seu carro está novo!') #todo comando que estiver com TAB depois dos ":", vai ser executado de acordo coma condição.
else:
    print('Seu carro está velho!')
#exemplo usando a mesma linha
print('Seu carro está novo!'if tempo <= 3 else 'Seu carro está velho!') #quando for uma linha, não se coloca o ":" no final da condição.
print('__FIM__') #todo comando que estiver alinhado na esquerda, será sempre executado.