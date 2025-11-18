#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

num = int(input('Digite um número: '))
contador = 2
elemento_um = 0
elemento_dois = 1
print(elemento_um,elemento_dois,end=' ')
while contador != num:
    elemento_um += elemento_dois
    print(elemento_um,end=' ')
    contador += 1
    if contador !=num:
        elemento_dois += elemento_um
        print(elemento_dois,end=' ')
        contador += 1