#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um número para ver seu fatorial: '))
fator: int = num - 1
total = 0
while fator != 1:
    if fator == num - 1:
        total += num * fator
        print(f'{num}x{fator} = {total}')
        fator -= 1
    else:
        print(f'{total}x{fator} = {total * fator}')
        total *= fator
        fator -= 1
print(f'Valor total da fatoração:\n{num}! = {total}')