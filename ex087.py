# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

matriz = []
linha = []
par = soma_coluna = maior_valor = 0
for c in range(3):
    for cont in range(3):
        linha.append(int(input(f'Digite um valor para [{c},{cont}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('*-'*30)
for p in matriz:
    for i in range(3):
        print(f'[ {p[i]} ]',end='' if i != 2 else '\n')
        if p[i] % 2 == 0:
            par += p[i]
print('-*'*30)
print(f'A soma dos valores pares é {par}')
for pos, c in enumerate(matriz):
    soma_coluna += c[2]
    if c == matriz[1]:
        for m in c:
            if m > maior_valor:
                maior_valor = m
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')