# Criando Exceções - Classes de erros personalizados no python

class TaErradoErros(Exception):
    pass


def testar():
    raise TaErradoErros('Errado')

try:
    testar()
except TaErradoErros as error:
    print(f'Erro: {error}')

