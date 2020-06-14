# OS + SHUTIL - Mover, copiar e apagar arquivos.

import os
import shutil

caminho_original = r'D:\Filmes\testepython'
caminho_novo = r'D:\Filmes\testepython2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_filew_path = os.path.join(caminho_novo, file)
        
        ## mover arquivo de um diretório para outro.
        #shutil.move(old_file_path,new_filew_path)
        ## copiar um arquivo de um diretório pra outro
        #shutil.copy(old_file_path,new_filew_path)

        # para apagar os arquivos do diretório
        os.remove(new_filew_path)
        
        print(f'Arquivo: {file} processado com sucesso:')




