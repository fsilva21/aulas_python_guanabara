#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: Número: 6.127 Print: 6

'''from math import trunc
num = float(input('Digite um número flutuante: '))
print(f'A porção inteira de {num} é {trunc(num)}')'''

num = float(input('Digite um número flutuante: '))
print(f'A porção inteira de {num} é {int(num)}')