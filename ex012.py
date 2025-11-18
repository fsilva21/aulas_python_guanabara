#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05

print(f'O produto custa R${preco}. Novo preço do produto, com 5% de desconto: R${preco-desconto:.2f}')
