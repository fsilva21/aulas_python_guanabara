#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de tres e que se encontram no intervalo de 1 até 500

soma = 0
contador = 0
for c in range(0,501,3):
    if c % 2 == 0:
        c += 0
    else:
        soma += c
        contador += 1
print(f'A soma dos {contador} valores é de {soma}')