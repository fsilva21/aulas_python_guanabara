# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos.

gols = []
total = 0
jogador = {'nome': str(input('Nome do jogador: ')), 'gols': gols}
partidas = int(input(f'Partidas que {jogador['nome']} jogou: '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c +1}?')))
    total += gols[c]
jogador['total'] = total
print('*-'*20)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for pos, i in enumerate(jogador['gols']):
    print(f'{"-> ":>5}Na partida {pos +1}, fez {i} gol(s).')
print(f'Foi um total de {jogador['total']} gols.')