#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for ímpar, desconsidere

soma = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os números pares totaliza {soma}')
