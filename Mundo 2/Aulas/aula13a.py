#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é uma estrutura versátil e simples de entender. 

# O for so conta até o penultimo numero, nesse caso o numero 4 não imprime.
for c in range(0, 4): 
     print(c)
print('Acabou 1')

# Para fazer a contagem regressiva, colocar o -1 na segunda virgula:
for c in range(4, 0, -1): 
     print(c)
print('Acabou 2')


# Para pular a contagem, colocar a quantidade de pulos depois da segunda virgula:
for c in range(0, 7, 2): 
     print(c)
print('Acabou 3')

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f, p):
    print(c)
print('Fim do input!')