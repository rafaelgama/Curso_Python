# Sistemas de perguntas e respostas com dicionários Python.

perg = {
    'Pergunta 1': {
        'pergunta':'Quanto é 2+2?',
        'respostas': {'a':'1','b':'4','c':'5',},
        'resposta_certa':'b',
    },
    'Pergunta 2': {
        'pergunta':'Quanto é 3+2?',
        'respostas': {'a':'4','b':'10','c':'6',},
        'resposta_certa':'c',
    },
}

res_certas = 0
for pk, pv in perg.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    rep_usr = input('Sua Resposta: ')
    if rep_usr == pv['resposta_certa']:
        print('EEEEHHH!!! Você acertou!!')
        res_certas += 1
    else:
        print('IXIIIII!!! Voce Errou!')

    print()
qtd_perg = len(perg)
perc_act = res_certas/qtd_perg * 100

print(f'total de perguntas são {qtd_perg}. ')
print(f'Voce acertou {res_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {perc_act:.2f}%.')
