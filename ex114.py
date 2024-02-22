import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31m O site Pudim não está acessível no momento.\033[m')
else:
    print('\033[36mConsegui acessar o site Pudim com sucesso!\033[m')