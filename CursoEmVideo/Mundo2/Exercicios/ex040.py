#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media < 5:
    print('Sua nota média foi {:.1f}, por isso voce está {}REPROVADO{}.'.format( media, cores['bvermelho'], cores['limpa']))
elif media >= 5 and media <= 6.9:
    print('Sua nota média foi {:.1f}, por isso voce está de {}RECUPERAÇÃO{}.'.format(media, cores['roxo'], cores['limpa']))
else:
    print('Sua nota média foi {:.1f}, por isso voce já está {}APROVADO{}.'.format(media, cores['bverde'], cores['limpa']))



print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)