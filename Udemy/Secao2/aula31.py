# While/else - repetição com acumuladores.

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 15:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no Else')
print('Fim do programa')