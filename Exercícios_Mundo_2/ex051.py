#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
for c in range(0,10):
    if c == 9:
        print(termo)
    else:
        print(termo, end=", ")
        termo += razao
