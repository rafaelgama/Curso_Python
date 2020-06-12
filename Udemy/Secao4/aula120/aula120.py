# impletando um iterator

class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    # para poder retornar a lista quando pedir o indice direto ex: lista[0]
    def __getitem__(self, index):
        return self.__items[index]

    # metodo para poder alterar um valor atribuindo ele direto pelo indice
    # como no exemplo: lista[1] = valor
    def __setitem__(self, index, valor):
        # verifica se estouro o indice, e dar um append para não dar erro.
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor
    
    # metodo para deletar por indice o valor da lista
    def __delitem__(self, index):
        del self.__items[index]

    # metodo para fazer a iteração da lista
    def __iter__(self):
        return self

    #metodo para retornar o próximo valor
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        # cria essa excessão para não estourar o erro quando chamar um proximo valor que não existe
        except IndexError:
            raise StopIteration

    # força retornar um print quando instancia a classe
    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    # metodo para retornar o print da classe somente com os valores.
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Rafael')
    lista.add('Gama')

    print(lista)
    lista[0] = 'Macedo'
    # Adcionando um valor em indice que não existe ainda
    lista[2] = 'Junior'

    del lista[2]

    print(lista)

    #print(lista)

    # transformando o Iterador em List() = lista - para imprimir mais de uma vez
    lista = list(lista)

    for valor in lista:
        print(valor)

    for valor in lista:
        print(valor)




