# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# função voto()
def voto(anonas):
    """Função para calcular a idade de voto

    Arguments:
        anonas {int} -- (OBRIGATÓRIO) - ano de nascimento
    """
    from datetime import datetime 
    anoatu = datetime.now().year
    if anonas < 0:
        anonas = 0
    age = anoatu - anonas
    print(age)
    if age < 16:
        print(f'Com {age} anos: NÃO VOTA!')
    elif (16 <= age < 18) or age >= 65:
        print(f'Com {age} anos: VOTO OPCIONAL!')
    elif 18 <= age < 65:
        print(f'Com {age} anos: VOTO OBRIGATÓRIO!')

#chamada da função
ano = int(input('Em qual ano você nasceu? '))
voto(ano)


print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)