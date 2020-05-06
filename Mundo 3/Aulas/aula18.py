# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

teste = list()
teste.append('Rafael')
teste.append(40)
galera = list()
galera.append(teste[:]) # é necessário sempre fazer uma cópia, se não colocar o [:], ele apenas vai referenciar.
teste[0] = 'Gama'
teste[1] = 42
galera.append(teste[:])
print(galera)

print('-=-'*10)
# Mostrando como imprimir os dados
pessoas = [['João',23],['Maria',24],['Joaquim',30],['Paulo',18]]
for g in pessoas:
    print(f'{g[0]} tem {g[1]} anos de idade.')

print('-=-'*10)
# Mostrando outra fomra de manipular os dados
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for d in galera:
    if d[1] >= 21:
        print(f'{d[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{d[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

print('-=-'*10)