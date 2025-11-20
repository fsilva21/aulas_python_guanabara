# Faça um mini-sistema que utilize o Interactive Help "help()" do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: Use cores!

from colorama import init, Fore, Back
from time import sleep
init(autoreset=True)
def titulo(msg):
    tam = len(msg) + 4
    print(Back.GREEN + '*' * tam)
    print(Back.BLACK + f'  {msg}  ')
    print(Back.GREEN + '*' * tam)
    sleep(1)

def ajuda(c):
    help(c)
    sleep(1)


#Programa principal
while True:
    pergunta = input(Fore.BLACK + Back.LIGHTBLUE_EX + 'Função ou Biblioteca > ').strip()
    if pergunta.upper() == 'FIM':
        f='ENCERRANDO PROGRAMA...'
        print(Back.RED + '~' * len(f))
        print(Back.RED + f'{f}')
        print(Back.RED + '~' * len(f))
        sleep(1)
        break
    titulo(f'Acessando o manual do comando \'{pergunta}\'')
    ajuda(pergunta)
