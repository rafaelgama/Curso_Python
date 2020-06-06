# Aula de Classes- Python orientado a Objetos

from pessoa import Pessoa

# Exemplo com parametro
p1 = Pessoa('Rafael',29)
p1.comer('Banana')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('doce')
p1.parar_falar()

# são independentes cada instancia
p2 = Pessoa('Gama',40)
print(p2.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# exemplo 1
#p1.nome = 'Luiz'
#p2.nome = 'João'



