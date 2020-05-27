"""
Operadores Lógicos - aula 22
and, or, not, in e not in
"""

usuario = input("Nome de usuário ")
senha = input("Senha de usuário ")
 
 
usuario_db = ('rafael')  # usuario database
senha_db = ('123456')       # senha database
 
if usuario == usuario_db and senha == senha_db:
    print(f"Olá {usuario}")
else:
    print("Você não está cadastrado na nossa base de dados.")