# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela

valores = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        valores.append(valor)
        print('Primeiro valor adicionado com sucesso na lista')
        continue
    for pos in range(len(valores)):
        if valor <= valores[pos]:
            valores.insert(pos,valor)
            print(f'Valor inserido na posição {pos}')
            break
    else:
        valores.append(valor)
        print('Valor inserido na última posição')
    print(valores)




























