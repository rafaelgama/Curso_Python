#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ' )).strip()  #poderia usar o lower() aqui e eliminar no print
print('A letra "A" aparece {} vezes'.format( frase.lower().count("a")) )
#soma 1 para aparecer o numero correto começando a contagem com 1
print('A primeira posição que letra "A" aparece é {}'.format( frase.lower().find('a')+1 )  ) #find() faz a busca da esquerda para a direita
print('A última posição que letra "A" aparece é {}'.format( frase.lower().rfind('a')+1 )  ) #rfind() faz a busca da direita para a esquerda