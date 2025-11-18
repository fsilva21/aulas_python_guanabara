#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo

print('Esse programa verifica se 3 retas formam um triângulo')
reta1 = float(input('Medida da primeira reta: '))
reta2 = float(input('Medida da segunda reta: '))
reta3 = float(input('Medida da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Essas retas formam um triângulo')
else:
    print('Essas retas NÃO formam um triangulo')