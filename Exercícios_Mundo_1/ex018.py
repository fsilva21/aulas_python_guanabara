#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite o angulo desejado: '))
rad = math.radians(angulo)
print(f'Seno{math.sin(rad)}')
