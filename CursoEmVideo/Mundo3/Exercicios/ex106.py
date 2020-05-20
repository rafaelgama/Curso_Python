# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


c = ('\033[m','\033[1;32m','\033[1;31m','\033[7:30m')


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# definição da função
def ajuda(com):    
    titulo(f'Acessando o manuel do comando: {com} ', 3)
    print(c[3],end='')
    help(com)
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('-=' * tam )
    print(f'  {msg}')
    print('-=' * tam )
    print(c[0],end='')

# programa principal.
comando = ''
while True:
    titulo("SSITEMA DE AJUDA PyHELP",1)
    comando = str(input('Função ou Biblioteca> ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')        

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)