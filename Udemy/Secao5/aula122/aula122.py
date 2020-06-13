from datetime import datetime
from locale import setlocale, LC_ALL # para trazer a localidade.
from calendar import mdays # vai retornar quantos dias tem cada mês.

# essa fução seta a localidade padrão do computador, caso o segundo parametro esteja
# em branco ou preencha o parametro par definir a localidade.
setlocale(LC_ALL, 'pt_br.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m')) # peago o mes atual e converte pra int()
formatacao1 = dt.strftime('%A,%d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

# mdays é um lista dizendo quantos dias tem cada mês do ano 
# começando pela posição 1 da lista.
print(mdays)
print(mes_atual, mdays[mes_atual])