# iterando strings com while em python.

# strings são imutáveis!!
mstring = ' o rato roeu a roupa do rei de roma.'
tam = len(mstring)

print(mstring.count('a'))

string2 = ''

c = 0 
while c < tam:
        
    if mstring[c] == 'r': # parar remover o r da frase
        string2 = string2 + mstring[c].upper()
    else:
        string2 = string2 + mstring[c]

    c += 1
print(string2)