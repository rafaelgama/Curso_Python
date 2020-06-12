# Datetime - Trabalhando com data e hora em Python
# https://docs.python.org/2/library/datetime.html

from datetime import datetime, timedelta

"""
data = datetime(2019, 4, 20, 10, 53, 20)
print(data)
# strftime() - metodo para formatar a data (datetime para str) de acordo com as Diretivas
print(data.strftime('%d/%m/%Y %H:%M:%S'))
"""
"""
# strptime() - converte uma data de str para datetime
data = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data)
# pegar o timestamp - contagem de segundos desde 1970 até a data do par
print(data.timestamp())
# converter o timestamp para datetime
data2 = datetime.fromtimestamp(1555729200.0)
print(data2)
"""

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# timedelta() - Acrescentar valores no objeto
data = data + timedelta(days=5, seconds=59)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
# é possivel fazer calculos nos parametros
data = data + timedelta(seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
# fazer calculos com o datetime
dif = d2-d1 # Dif so carrega a diferença das horas.
print(dif)
# ver somentes valores especificos
print(dif.seconds, dif.total_seconds(), dif.days)
#ver so a hora
print(d1.time())
# comparar datas
print(d2 < d1)





