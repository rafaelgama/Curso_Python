"""
Operadores Ralacionais - Aula 21
== igualdade
> maior que 
>= maior que ou igual a
< meno que
<= menor que ou igual a
!= diferente
"""

idade = """40"""
idade = int(idade)
print(f'Idade {idade}', type(idade))



print('    Seja bem vinda ao cadastro para empréstimo! ')
 
nome = input('Digite seu Nome Completo: ')
idade = int(input('Sua idade: '))
cpf = int(input('CPF: '))
 
maior = 18
 
if idade >= maior:
    agencia = (input('Agência com dígito: '))
    conta = (input('Conta: '))
    banco = input('Banco: ')
    print('Seu emprestimo foi liberado no valor de 2 mil reais! ')
else:
    print('Desculpe, você é menor de idade! ')