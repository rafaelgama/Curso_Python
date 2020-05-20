# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. 
# Aprenda como usar a estrutura try except no Python de uma forma simples.

# Tratamentos de excessão para mostrar o erro definindo a mensagem para tipo de erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b

except (ValueError,TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados que vc digitou :(')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O Usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O Problema encontrado foi {erro.__class__}')
else:    
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte Sempre!')
