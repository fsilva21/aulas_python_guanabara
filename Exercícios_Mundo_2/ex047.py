#Faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
from itertools import count

print('Números pares entre 1 e 50')
contador = 0
for c in range(2,51,2):
    print('.',end=" ")
    if c % 2 != 0:
        c += 1
    else:
        print(c,end=' ')
        contador += 1
print(f"\nExistem {contador} números pares entre 1 e 50")
