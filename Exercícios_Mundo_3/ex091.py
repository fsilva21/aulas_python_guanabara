# Crie um programa onde 4 jogadores joguem um dado (1 a 6) e tenham resultados aleatórios, guardando os resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
print('Valores sorteados:')
sleep(1)
for k, v in jogadores.items():
        print(f'{"":>5}O {k} tirou {v}')
        sleep(1)
print('Ranking dos jogadores:')
sleep(1)
ranking = sorted(jogadores.values(), reverse=True)
for c in range(4):
    for k, v in jogadores.items():
        if v == ranking[c]:
            print(f'{c+1:>5}º lugar: {k} com {v}')
            sleep(1)
            del jogadores[k]
            break
