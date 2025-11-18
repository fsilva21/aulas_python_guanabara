# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única, que mantenha separados os pares e impares.
# No final, mostre as duas listas, de pares e impares em ordem crescente (são 2 listas de pares e impares dentro de uma maior)

valores = list()
pares = list()
impares = list()
for c in range(7):
    valor = int(input(f'Digite o {c + 1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
valores.append(pares[:])
valores.append(impares[:])
print(f'Lista de valores pares: {valores[0]}')
print(f'Lista de valores impares: {valores[1]}')
