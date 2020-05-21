cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


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

