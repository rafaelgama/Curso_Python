#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input("Informe um número: "))
print('Analisando o número {}'.format(num))
#maneira de resolver de forma matemática
u = num // 1 % 10       #Utiliza Divisão inteira e depois utiliza o resto da divisão.
d = num // 10 % 10      #Utiliza Divisão inteira e depois utiliza o resto da divisão.
c = num // 100 % 10     #Utiliza Divisão inteira e depois utiliza o resto da divisão.
m = num // 1000 % 10    #Utiliza Divisão inteira e depois utiliza o resto da divisão.
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#Maneira de resolver transfomando em String, mas fica limitado a sempre existir 4 char.
#n = str(num)
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))