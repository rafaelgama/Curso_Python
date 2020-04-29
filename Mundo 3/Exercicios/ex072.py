# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
            'quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20: 
        break
    print('Tente novamente')

print(f'Voce digitou o número {extenso[num]}')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)