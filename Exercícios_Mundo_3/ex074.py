# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint

sorteio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
contador = 0
print(f'Os valores sorteados são:', end=' ')
for numero in sorteio:
    print(numero, end=' ')
    if contador == 0:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    contador += 1
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
#Resolução otimizada
lista = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
organizado = (sorted(lista))
print(f'\n→ Os números gerados foram: {lista}.')
print(f'→ O menor número foi {organizado[0]}.')
print(f'→ O menor número foi {organizado[4]}.')