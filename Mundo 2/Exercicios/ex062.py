#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' PROGRESSAO ARITIMETICA 2 ')) # centraliza(^) o texto no meio do caracteres de '='

pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pri
qtd = 10
tot = 0
while qtd != 0:    
    cnt = 1
    while cnt <= qtd:
        print('{}'.format(termo), end=' -> ')
        termo += raz
        cnt += 1
        tot += 1
    print('PAUSA')
    qtd = int(input('Quanto Termos você quer mostrar mais? '))
print('Progressão finalizado com {} termos mostrados.'.format(tot))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)