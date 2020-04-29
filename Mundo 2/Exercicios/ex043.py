#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/(altura**2)

print("Com o peso {:.2f}Kg e a altura de {:.2f}m, seu IMC é {:.2f} e seu resultado: ".format(peso, altura, imc))
if imc < 18.5:
    print(cores['roxo']+'ABAIXO DO PESO!'+cores['limpa'])
elif imc < 25:
    print(cores['bverde']+'PESO IDEAL!'+cores['limpa'])
elif imc < 30:
    print(cores['roxo']+'SOBREPESO!'+cores['limpa'])
elif imc < 40:
    print(cores['bvermelho']+'OBESIDADE!'+cores['limpa'])
else:
    print(cores['bvermelho']+'OBESIDADE MÓRBIDA!'+cores['limpa'])        

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)