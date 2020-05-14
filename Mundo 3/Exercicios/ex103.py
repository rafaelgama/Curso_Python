# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# função ficha()
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} no campeonato.')


# Programa Principal
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)