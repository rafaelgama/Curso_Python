# Modulo OS - Percorrendo arquivos e Pastas.
# https://docs.python.org/3/library/functions.html#open

import os

#'C:\Temp\Formula de Lançamento 7.0 - 2018\Ferramentas'
caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

# função para converter os valores com origem em bytes
def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:        
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'        
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho,2)
    return f'{tamanho}{texto}'.replace('.',',')

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        # verifica se o termo está contido na string de algum arquivo.
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho completo:', caminho_completo)
                print('Nome:', arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido',e)

print()
print(f'{conta} arquivo(s) encontrado(s)')
            








