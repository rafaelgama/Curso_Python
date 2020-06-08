# Metaclasses
# Em Python tudo é um objeto: incluindo classes
# Metaclasses são as "Classes" que criam classes.
# type é uma metaclasse (!!??)

# attr = Atributo de classe

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa ciar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'B_fala precisa ser um método, não atributo em {name}.')

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        print(namespace)
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'
    def fala(self):
        self.b_fala()


class B(A):
    attr_classe = 'Valor B'
    def b_fala(self):
        print('OI')


b = B()
print(b.attr_classe)

# Metaclasses são classes que criam outras classes.
# Exemplo 2 - type cria sozinho uma metaclasse

class Pai:
    nome = 'Teste'

D = type('D', (Pai,), {'attr':'Olá Mundo!'})

d= D()
print(type(d))
print(d.nome)