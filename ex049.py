#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, utilizando o laço for

from time import sleep
print('Tabuada')
sleep(1)
num = int(input('Escolha o número para multiplicar: '))
fim = int(input('Escolha o segundo fator da multiplicação: '))
tabuada = 0
for c in range(0,fim+1,1):
    tabuada = num * c
    print(f'{num} * {c} = {tabuada}')