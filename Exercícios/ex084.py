# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves

pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    pergunta = str(input('Quer continuar [S/N]? ')).upper().strip()
    while pergunta not in 'SN':
        pergunta = str(input('Digite uma opção válida [S/N]: ')).upper().strip()
    if pergunta == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
for pos, c in enumerate(pessoas):
    if pos == 0:
        maior = menor = c[1]
    else:
        if c[1] > maior:
            maior = c[1]
        elif c[1] < menor:
            menor = c[1]
print(f'O maior peso foi de {maior}Kg, pertencente a ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {menor}Kg, pertencente a ',end='')
for p in pessoas:
        if p[1] == menor:
            print(f'[{p[0]}] ',end='')