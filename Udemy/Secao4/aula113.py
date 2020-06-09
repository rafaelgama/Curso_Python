# DocStrings - Documentação do Python

def uma_linha():
    """ Documentação de uma linha!"""
    return 1

#help(uma_linha)

# Typing - https://docs.python.org/3/library/typing.html

# para definir qual o tipo da variavel, coloca o tipo depois dos ":"
x: int = 10
y: float = 10.5
z: bool = False

# como pode ser definido o tipo na entrada, pode ser definido o tipo
# no retorno na função tb, colocando "-> + type", ex:
"""def func_ret(p1: float, p2: str, p3:dict) -> float:
    return 10.5
"""
# Para definir o tipo do retorno com mais de um tipo ao mesmo tempo

from typing import Union

def func_tip() -> Union[list, dict]:
    return []






