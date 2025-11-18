# Faça um programa que tenha uma lista chamada números e duas funções chamadas "sorteia()" e "somaPar()".
# A primeira função vai sortear 5 números e vai colocar em uma lista.
# A segunda vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(num):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(5):
        num[c] = randint(0,10)
        print(num[c],end=' ')
        sleep(0.5)
    print('Pronto!')
    sleep(0.5)
def somaPar():
    soma = 0
    for par in valores:
        if par % 2 == 0:
            soma += par
    print(f'Somando os valores pares de {valores} temos o número: {soma}')


valores = list(range(5))
sorteia(valores)
somaPar()