#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
resto = 0
for c in range(2,num):
    resto = num % c
    if resto == 0:
        print(f'{num} não é um número primo!')
        exit()
print(f'{num} é um número primo!')