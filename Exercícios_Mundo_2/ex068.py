#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final.

from random import randint
from time import sleep

tentativas = 0
while True:
    num_ia = randint(0,10)
    #Loop de verificação de 0 a 10
    while True:
        num_jogador = int(input('Número de 0 a 10: '))
        if 10 >= num_jogador >= 0:
            break
        else:
            print('Número inválido...')
    #Atribuidor de Ímpar e Par para jogador e IA
    while True:
        escolha_jogador = str(input('Ímpar ou par? [I/P]: ')).upper().strip()[0]
        if escolha_jogador in 'IP':
            break
        else:
            print('Escolha inválida, tente novamente!')
    print('Você:..Par!' if escolha_jogador == 'P'  else 'Você:..Ímpar!')
    sleep(1.5)
    if escolha_jogador in 'pP':
        escolha_ia = 'I'
        print('Máquina:..Ímpar!')
    elif escolha_jogador in 'iíIÍ':
        escolha_ia = 'P'
        print('Máquina:..Par!')
    sleep(1.5)
    #Verificação lógica do jogo (Vitória ou derrota)
    print(f'Você escolhe: {num_jogador}')
    sleep(1.5)
    print(f'Máquina escolhe: {num_ia}')
    sleep(1.5)
    #Se der Par:
    if (num_jogador + num_ia) % 2 == 0:
        if escolha_ia == 'P':
            print('Vencedor: Máquina (PAR)')
            sleep(1)
            print('Que pena, você perdeu..')
            sleep(1)
            print('Máquina: Hahaha, verme insolente, achou que ganharia?')
            break
        elif escolha_ia == 'I':
            print('Vencedor: Jogador (PAR)')
            print('Máquina: Urgh.. Isso não vai ficar assim!')
            sleep(1)
            print('Máquina: Denovo!!')
            tentativas += 1
    #Se der Ímpar:
    if (num_jogador + num_ia) % 2 == 1:
        if escolha_ia == 'P':
            print('Vencedor: Jogador (ÍMPAR)')
            print('Máquina: Urgh.. Isso não vai ficar assim!')
            sleep(1)
            print('Máquina: Denovo!!')
            tentativas += 1
        elif escolha_ia == 'I':
            print('Vencedor: Máquina (ÍMPAR)')
            sleep(1)
            print('Que pena, você perdeu..')
            sleep(1)
            print('Máquina: O resultado esperado...')
            break
sleep(1.5)
print(f'Você ganhou {tentativas} vez(es)!!')
