# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python 
# e reutilizar nossos códigos em outros projetos. 
# Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.

# Para o Python, todo fonte pode ser um módulo. Agora para se criar Pacotes, serão necessários folders contendo os foldes e funções dentro.
# no momento do import, se existir funções com o mesmo nome, o que vale é ultima a ser importada.

import aula22_ut
# programa Principal.
num = int(input('Digite um valor: '))
fat = aula22_ut.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {aula22_ut.dobro(num)}')

