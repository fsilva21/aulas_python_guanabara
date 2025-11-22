#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dolar = 3.27
carteira = float(input('Quanto dinheiro você tem na carteira? '))

print(f'Com R${carteira} você pode comprar ${carteira / dolar:.2f}')