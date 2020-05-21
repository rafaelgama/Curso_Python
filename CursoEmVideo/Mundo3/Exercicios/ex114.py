# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLERROR:
    print('O site Pudim não está acessível!')
else:
    print('consegui Acessar o site Pudim com sucesso!')
    #print(site.read()) - comando para a acessar o conteúdo HTML da página.

