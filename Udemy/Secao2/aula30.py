"""
While em python - Aula 30

"""
x = 0 
while x < 10:
    if x == 3:
        x += 1
        continue # funciona como o loop em ADVPL, ele pula o laço que está sendo excutado.
    if x == 8:
        break # funciona como o exit emADVPL, ele finaliza o loop.
    print(x)
    x += 1


