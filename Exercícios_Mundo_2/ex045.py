#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

cores = {'verde':'\033[1;32m' , 'vermelho': '\033[1;31m'}
print('Vamos jogar Jokenpô ?')
sleep(0.4)
opcao_jogador = int(input('Escolha uma opção:\n(1) Pedra\n(2) Papel\n(3) Tesoura\nOpção desejada: '))
opcao_IA = randint(1,3)
print('Você escolheu.',end="")
sleep(0.7)
print('.',end='')
sleep(0.7)
print('.',end=''),sleep(0.7)
if opcao_jogador == 1:
    print('PEDRA!')
elif opcao_jogador == 2:
    print('PAPEL!')
elif opcao_jogador == 3:
    print('TESOURA!')
else:
    print('Opção inválida\nJogo encerrado')
    exit()
sleep(0.7)
print('Preparado?'),sleep(0.7)
print('JO',end=""),sleep(0.7)
print('KEN',end=""),sleep(0.7)
print('PO'),sleep(0.4)
print('-='*20)
print('O oponente escolheu.',end=""),sleep(0.7)
print('.',end=""),sleep(0.7)
print('.',end=""),sleep(0.7)
if opcao_IA == 1:
    print('.PEDRA!')
elif opcao_IA == 2:
    print('.PAPEL!')
elif opcao_IA == 3:
    print('.TESOURA!')
print('-='*20)
sleep(0.4)
if opcao_jogador == 1 and opcao_IA == 3 or opcao_jogador == 2 and opcao_IA == 1 or opcao_jogador == 3 and opcao_IA == 2:
    print(f'{cores['verde']}VITÓRIA!')
elif opcao_jogador == opcao_IA:
    print('EMPATE')
else:
    print(f'{cores['vermelho']}DERROTA')