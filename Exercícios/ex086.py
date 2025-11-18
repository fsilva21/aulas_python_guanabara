# Crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta.

matriz = []
linha = []
for c in range(3):
    for cont in range(3):
        linha.append(int(input(f'Digite um valor para [{c},{cont}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('*-'*30)
for p in matriz:
    for i in range(3):
        print(f'[ {p[i]:^5} ]',end='' if i != 2 else '\n')