#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt,hypot
cat_oposto = float(input('Qual o comprimento do cateto oposto? '))
cat_adjacente = float(input('Qual o comprimento do cateto adjacente? '))
'''hipotenusa = (cat_oposto**2+cat_adjacente**2)
print(f'O valor da hipotenusa deste triângulo é {sqrt(hipotenusa):.2f}')'''
hipo = hypot(cat_oposto,cat_adjacente)
print(f'O valor da hipotenusa é {hipo}')