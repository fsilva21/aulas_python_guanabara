# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    maior_num = 0
    print('*-'*30)
    print('Analisando os valores passados...')
    sleep(1)
    for c in num:
        print(f'{c}',end=' ')
        sleep(0.5)
        if c == num[0]:
            maior_num = c
        elif c > maior_num:
            maior_num = c
    print(f'Foram informados {len(num)} valores ao todo')
    sleep(0.5)
    print(f'O maior número informado foi {maior_num}')
    sleep(1)


maior(6,4,2,3)
maior(7,2,9,0,1,12,66,24)
maior(8)
maior()
