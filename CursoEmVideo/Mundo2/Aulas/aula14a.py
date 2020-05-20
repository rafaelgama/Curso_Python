#Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.

# exemplo simples, para colocar no lugar do FOR, quando voce sabe o fim
c = 1
while c <= 10:
    print(c)
    c += 1
print('Fim')

# exemplo de loop quando não se sabe o fim.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares.'.format(par,impar))
print('Fim')