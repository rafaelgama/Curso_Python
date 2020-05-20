# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. 
# Aprenda como usar a estrutura try except no Python de uma forma simples.

# Tratamentos de excessão para mostrar o erro sem definir antes
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b
# colocando somente o "except" não é mostrado o erro, mas colocando no exemplo abaixo ele carrega na variável.    
except Exception as erro:
    #print('Infelizmente tivemos um problema :(')
    print(f'O Problema encontrado foi {erro.__class__}')
else:    
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte Sempre!')
