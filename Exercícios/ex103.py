# Faça um programa que tenha uma função chamada "ficha()", que receba dois parâmetros opcionais: o nome de um jogador e quantos gols marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(n,g):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = int(0)
if not nome.isalpha():
    nome = '<desconhecido>'
ficha(nome,gols)