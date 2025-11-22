# Faça um programa que ajuda um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e sorteará 6 números entre 1 e 60 para cada jogo (SEM REPETIR NO MESMO JOGO), cadastrando em uma lista composta

from random import randint
from time import sleep
print('*'*20,'GERADOR DE JOGOS DA MEGA SENA','*'*20)
qtd_jogos = int(input('\nDigite a quantidade de jogos desejados: '))
lista_jogos = []
numeros = []
num = 0
print('=-='*5,f'Sorteando {qtd_jogos} jogos','=-='*5)
sleep(1)
for i in range(qtd_jogos):
    while len(numeros) < 6:
        num = randint(1,60)
        if len(numeros) == 0:
            numeros.append(num)
        else:
            for c in range(len(numeros)):
                if num == numeros[c]:
                    break
            else:
                numeros.append(num)
    numeros.sort()
    lista_jogos.append(numeros[:])
    numeros.clear()
for pos, j in enumerate(lista_jogos):
    print(f'Jogo {pos + 1}: ', j)
    sleep(1)
print('=-='*5,'BOA SORTE!','=-='*5)