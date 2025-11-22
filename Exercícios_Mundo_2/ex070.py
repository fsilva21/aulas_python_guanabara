#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# - Qual é o total gasto na compra
# - Quantos produtos custam mais de R$ 1000
# - Qual é o nome do produto mais barato

total = caro = 0
nome = str(input('Nome do produto: '))
preco = float(input('Preço: R$ '))
preco_barato = preco
nome_barato = nome
while True:
    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    total += preco
    if preco > 1000:
        caro += 1
    while True:
        resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resposta in 'SN':
            break
        else:
            print('Digite uma opção válida.')
    if resposta == 'N':
        break
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
print(f'O total gasto foi R${total:.2f}')
print(f'{caro} produtos custam mais de R$1000')
print(f'{nome_barato} foi o produto mais barato comprado')
