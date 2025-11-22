#Melhore o jogo desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Bem vindo ao jogo da adivinhação v2.0\nEu sempre penso em um número de 0 a 10... Consegue adivinhar?')
num_jogador = -1
num_ia = randint(0,10)
palpites = 0
while num_jogador != num_ia:
    num_jogador = int(input('Digite um número (0 a 10): '))
    if num_jogador > 10 or num_jogador < 0:
        print('ERRO 404 FORBIDDEN \n(ENTRE COM UM NÚMERO INTEIRO DE 0 A 10)')
    else:
        if num_jogador < num_ia:
            print('Mais...Tente denovo.')
        elif num_jogador > num_ia:
            print('Menos...Tente denovo.')
        palpites += 1
print(f'Parabéns!\nVocê ganhou com {palpites} palpites!!')
