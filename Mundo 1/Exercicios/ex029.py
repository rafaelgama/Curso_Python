#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velo = float(input('\033[;33mQual a velocidade do carro? \033[m'))
if velo <= 80:
    print('\033[;34mVoce está dentro da velocidade permitida de até 80Km/h, digira com segurança.\033[m')
else:
    passou = velo-80
    multa = passou*7
    print("\033[;;41mA velocidade está {} km/h acima do permitido de 80km/h\033[m".format( passou ))
    print("Seu carro setá \033[1mmultado\033[m em R${:.2f} reais, pela infração.".format( multa ))

print('='*10)
print('\033[7;30m___FIM___\033[m')
print('='*10)