#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'roxo':'\033[35m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

salfunc = float(input(cores['limpa']+'Qual é o salário do funcionário?'+cores['roxo']+' '))
salnovo = salfunc*(10/100) + salfunc
if salfunc <= 1250:
    salnovo = salfunc*(15/100) + salfunc

print(cores['limpa']) # posso limpar as cores antes de imprimir
print('Quem ganhava {}R${:.2f}{} reais, passa ganhar agora {}R${:.2f}{} reais.'.format(cores['azul'],salfunc,cores['limpa'],cores['vermelho'],salnovo,cores['limpa']))


print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)