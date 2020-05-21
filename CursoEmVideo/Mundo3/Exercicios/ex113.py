# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# definição das funções
def leiaInt(var):    
    while True:
        try:  
            num = int(input(var))
        except (ValueError,TypeError):
            print(cores['bvermelho']+'ERRO! Digite um número inteiro válido!'+cores['limpa'])
            continue
        except KeyboardInterrupt:
            print(cores['bvermelho']+'Entrada de dados interrompida pelo usuário!'+cores['limpa'])
            return 0
        else:
            return num

def leiaFloat(var):
    while True:
        try:
            num = float(input(var))
        except (ValueError, TypeError):
            print(cores['bvermelho']+'ERRO! Digite um número Real válido!'+cores['limpa'])
            continue
        except KeyboardInterrupt:
            print(cores['bvermelho']+'Entrada de dados interrompida pelo usuário!'+cores['limpa'])
            return 0
        else:
            return num


# Programa principal
ni = leiaInt('Digite um número Inteiro: ')
nf = leiaFloat('Digite um número Real: ')
print(f'Voce acabou de digitar o número Inteiro {ni}.')
print(f'Você acabou de digitar o número Real {nf}.')

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)