# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, 
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, 
# escopo de variáveis e retorno de resultados. 

# Interactive Help
# pode ser digitado no console do Idle ou executado por programa, ai no terminal vc passa a pesquisa que quer fazer.
# por exemplo, ao digitar o Help(), na sequencia digite uma função pra pesquisar = print, len, input...etc.
# para finalizar, digite quit e o programa volta para o console.
#help()
# outra forma de executar o help é colocando a pesquisa por parâmetro:
print(f"{'Exemplo do comando help()':=^40}")
help(print)

# pode ser utilizado também o comando "__doc__" depois da função que vc quer consultar 
print(f"{'Exemplo do comando __doc__':=^40}")
print(len.__doc__)

# exemplo de docstrings
print(f"{'Exemplo do docstrings':=^40}")
# função contador()
def contador(i,f,p):
    '''
        Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += 1
    print('FIM!')

contador(2,10,2)
# Exibe a docstrings digitada
help(contador)



