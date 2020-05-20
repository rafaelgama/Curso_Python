#Manipulação de Strings
#Curso em Video Python = 21
#012345678901234567890 = 21
frase = 'Curso em Video Python'
print(frase)
#Fatiar as letras
print(frase[3]) #s
print(frase[3:13]) #so em Vide - Note que sempre a ultima posilçao é = (valor)-1
print(frase[:13]) #Curso em Vide - Note que sempre q não tiver valor, é pego o primeiro
print(frase[13:]) #o Python - Note que sempre q não tiver valor, é pego o ultimo
print(frase[1:13:2]) #us mVd - A Terceira casa ele vai utilizar para pular de casas de acordo com o valor digitado.
#imprimindo textos grandes - utiliza-se 3 aspas
print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), 
lower(), capitalize(), title(), strip(), junção com join().""")
#manipulando objetos
print(frase.count('o')) # conta a quantidade de caracteres passado por parametro. -Case Sensitive
print(frase.upper().count('O'))# transforma em maiusculo e depois conta o caractere. 
print(len(frase)) # conta a quantidade de caracteres.
print(len(frase.strip())) # conta a quantidade de caracteres, e o strip() remotve os espaços em brancos de inicio e do fim.
print(frase.replace('Python','Android')) #so imprime alteração, mas a string é imutavel.
frase = frase.replace('Python','Android') #alterando a string definitivo
print(frase)
print('Curso' in frase)#Forma de tratar o contido de caracteres dentro de uma frase.
print(frase.find('Video'))#devolve a posição da busca dentro da string quando encontra, caso o contrário  retorna -1.
print(frase.lower().find('video')) #tratamento para encontrar palavras quando não souber tamanho das letras - case sensitive
print(frase.split())  # transforma a frase em lista(array)
dividido = frase.split() # carrega em uma variavel a lista
print(dividido[2]) #imprime so a primeira posição da lista
print(dividido[2][2]) #imprime uma posição da string da lista