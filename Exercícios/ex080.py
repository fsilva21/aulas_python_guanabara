# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela

valores = []
contador = 0
while True:
    valor = int(input('Digite um valor: '))
    if contador == 0:
        valores.append(valor)
        print('Primeiro valor adicionado com sucesso na lista')
    else:
        for pos in range(len(valores)):
            if valor <= valores[pos]:
                valores.insert(pos,valor)
                print(f'Valor inserido na posição {pos}')
                break
        else:
            valores.append(valor)
            print('Valor inserido na última posição')
    contador += 1
    print(valores)
    if contador == 5:
        break





























