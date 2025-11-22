#Faça um programa que leia um ano qualquer e mostre se ele é bissexto (pesquisar a fórmula por trás)

from datetime import date
ano = int(input('Descubra se um ano qualquer é bissexto\nDigite o ano desejado ou "0" para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
elif ano % 100 == 0:
    print(f'O ano de {ano} NÃO é bissexto')
elif ano % 4 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'O ano de {ano} NÃO é um ano bissexto')