# Encapsulamento - POO
# public, protected, private
# convenções em python
# (0 underline) = para variaveis public
# _ (1 underline) = para variaveis protected - Vc inda consegue alterar, mas é recomendodo fortemente q não.
# __ (2 underlines) = para variáveis private - Vc não tem acesso a variável.

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    # para retornar um valor quando a variável for private
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
# para acessar a variável private utiliza dessa forma:
print(bd._BaseDeDados__dados)
# So funciona com private se tiver Getter e Setter ex:
print(bd.dados) 
bd.apaga_cliente(2)
bd.lista_clientes()
