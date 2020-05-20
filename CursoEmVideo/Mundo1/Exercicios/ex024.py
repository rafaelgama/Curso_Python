#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid = str(input('Em qual cidade que vc nasceu: ')).strip()  #Remove os espaços em branco na digitação.
print("O nome da cidade começa com SANTO? {}".format(cid[:5].upper() == 'SANTO')) #transforma tudo para maiúsculo