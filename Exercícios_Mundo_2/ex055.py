#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
lista_peso = []
for c in range(0,5):
    peso = int(input(f'Peso da {c+1}ª pessoa: '))
    lista_peso.append(peso)
    if menor_peso == 0:
        menor_peso = peso
    if lista_peso[c] > maior_peso:
        maior_peso = lista_peso[c]
    elif lista_peso[c] < menor_peso:
        menor_peso = lista_peso[c]
print(f'O maior peso registrado foi {maior_peso}Kg')
print(f'O menor peso registrado foi {menor_peso}Kg')
