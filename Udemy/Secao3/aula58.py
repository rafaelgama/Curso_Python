# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elemtentos apenas no set da esquerda)
# symetric_difference ^ (Elemtentos que estão nos dois sets, mas não em ambos)

#SETs são dicionários sem indices, chamados de CONJUNTOS em Pt-BR.
#SETs não respeitam ordem.
#SETs não aceitam valores duplicados.
# Criando um SET com valores
s1 = {1,2,3,4,5}
print(s1)
print('-=-' * 40)
#Criando um SET com comando
s2 = set()
s2.add(1) # adiciona valor
s2.add(2)
s2.add((1,2,3,'Rafa'))
s2.discard(2) # Remove o valor.
print(s2)
print('-=-' * 40)

#Remove valores duplicados em lista
l1 = [1,1,2,3,4,2,1,2,3,4,5,6,7,7,7,7,'Rafa','Rafa']
l1 = set(l1)
l1 = list(l1)
print(l1)
print('-=-' * 40)
#Funções para trabalha com o SET
sa = {1,2,3,4,5,7}
sb = {1,2,3,4,5,6}
#sc = sa | sb # union
#sc = sa & sb # intersecção, so vai juntar os SETs, caso existam nos dois.
#sc = sa - sb #Trata a diferença, pegando o SET da esquerda sempre.
sc = sa ^ sb #symetric_difference so vou trazer os valores que não estão nos dois SETs.

print(sc)

