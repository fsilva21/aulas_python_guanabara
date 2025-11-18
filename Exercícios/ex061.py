#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando o while

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
contador = 0
while contador != 10:
    print(termo, end=' ')
    termo += razao
    contador += 1