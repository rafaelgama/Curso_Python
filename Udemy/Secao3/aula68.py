# Zip - Unindo iteráveis
# Zip_longest - Itertools
from itertools import zip_longest, count

# O Zip une os Iteraveis com a mesma quantidade descartando o que sobra.
#Exemplos de ZIP
cidades = ['São Paulo','Belo horizonte','Salvador','Campinas']
estados = ['SP','MG','BA']

cid_est = zip(cidades, estados)
print(cid_est)
# transformar em lista de novo
#print(list(cid_est))

for valor in cid_est:
    print(valor)

print('-=-' * 20)

# O Zip_longest une os Iteraveis mesmo que não tenha a mesma quantidade
#Exemplos de Zip_longest
"""cid = ['São Paulo','Belo horizonte','Salvador','Campinas']
est = ['SP','MG','BA']

cidest = zip_longest(cid, est, fillvalue='Estado') #fillvalue é utilizado para preencher os que são vazios.
print(cidest)

for val in cidest:
    print(val)

print('-=-' * 20)"""

#Exemplos de Zip com count
ind = count()
cid = ['São Paulo','Belo horizonte','Salvador','Campinas']
est = ['SP','MG','BA']

cidest = zip(ind, est, cid) #fillvalue é utilizado para preencher os que são vazios.
print(cidest)

for val in cidest:
    print(val)
 




