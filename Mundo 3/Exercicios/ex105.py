# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
"""
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional) 
"""

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# Definição da função
def notas(* val, sit=False):
    """Função para analisar notas e situações do aluno.

    Keyword Arguments:
        val {list} -- uma ou mais notas dos alunos (aceita varias)
        sit {bool} -- (opcional) Indica ou não se deve mostrar a situação do aluno (default: {False})

    Returns:
        [dict] -- dicionário com várias informações sobre a situação do aluno.
    """
    notas = dict()
    qtd = mai = men = med = tot = 0
    for v in val:
        tot += v
        qtd += 1
        if mai < v or mai == 0:
            mai = v
        if men > v or men == 0:
            men = v
    med = tot / qtd
    notas['total'] = qtd
    notas['maior'] = mai
    notas['menor'] = men
    notas['media'] = med
    if sit:
        if notas['media'] >= 7:
            notas['situacao'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'

    return notas

# exemplo do guanabara
def notas2(* n, sit=False):
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n)/len(n)
    if sit:
        if notas['media'] >= 7:
            notas['situacao'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'

    return notas


# programa principal
resp = notas(5.5, 2.5, 1.5, 10, sit=True)
print(resp)
help(notas)

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)