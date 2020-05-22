# Criar Variáveis para nome (str), idade (int), altura(float) e peso(float) de uma pessoa.
# Criar a variável com ano atual (int)
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-Strings (com chaves)

nome  = 'Luiz'
idade = 32
altura = 1.70
peso = 82.5
ano_atual = 2019
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e sua altura é {altura:.2F}.')
print(f'{nome} pesa {peso} e seu imc é de {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')