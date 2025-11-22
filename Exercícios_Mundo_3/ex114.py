import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Site fora do ar.')
else:
    print('Tudo certo')
    print(site.read())
