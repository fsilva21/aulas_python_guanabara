#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
#o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep

num_ia = random.randint(0,5)
print('Bem vindo ao jogo da adivinhação')
num_player = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(1)
if num_player >5 or num_player <0:
    print('Erro (Digite um número entre 0 e 5)')
else:
    if num_player == num_ia:
        print(f'Número sorteado {num_ia}\nNúmero escolhido {num_player}')
        print('Parabéns, você ganhou!')
    else:
        print(f'Número sorteado {num_ia}\nNúmero escolhido {num_player}')
        print('Você perdeu')
