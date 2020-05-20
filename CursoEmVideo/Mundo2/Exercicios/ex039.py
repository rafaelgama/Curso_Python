#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
cores =  {'limpa':'\033[m',
            'bazulm':'\033[1;36m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'__INICIO__'+cores['limpa'])
print('-=-'*8)
# verifica o sexo da pessoa para o cadsatro
sexo = str(input('Digite seu sexo [ M ] - Mulher ou [ H ] - Homem :')).upper().strip()
if sexo == 'M':
    print('Voce está liberada do alistamento.')
elif sexo != 'H':
    print('Opção {} Inválida, digite novamente!'.format(sexo))
else: 
    #Executa o codigo quando a opção for H
    anonas = int(input(cores['limpa']+'Digite o seu ano de nascimento:'+cores['roxo']+' '))
    anoatu = datetime.date.today().year
    idade = anoatu - anonas
    print(cores['limpa']+'Quem nasceu em {}, tem {} anos de idade.'.format(anonas, idade)) 
    if idade > 18:
        print('Voce ja passou {} anos do prazo de alistamento, voce deveria ter se alistado em: {}.'.format(idade-18,anoatu-(idade-18)))
    elif idade == 18:
        print('Voce está na idade de se alistar!')
    else:
        if 18-idade == 1:
            print('Falta 1 ano para voce se alistar, seu alistamento será em: {}.'.format( anoatu+1 ))
        else:
            print('Faltam {} anos para voce se alistar, seu alistamento será em: {}.'.format( 18-idade, anoatu+(18-idade) ))


print('-=-'*8)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('-=-'*8)