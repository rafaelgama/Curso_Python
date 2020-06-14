# String - Template
# Criação de um Template em HTML

from string import Template
from datetime import datetime

path = r'D:\GitHub\Curso_Python\Udemy\Secao5\aula130'

with open(path+'\Template.html', 'r') as html:
    template = Template(html.read()) # Template dessa linha faz parte do modulo string
    data_atual = datetime.now().strftime('%d/%m/%Y')
    # o metodo substitute, levanta excessão se houver algum erro.
    # corpo_msg = template.substitute(nome='Rafael Gama',data=data_atual)
    # o metodo safe_substitute, não levanta excessão se houver algum erro.
    corpo_msg = template.safe_substitute(nome='Rafael Gama',data=data_atual)

print(corpo_msg)







