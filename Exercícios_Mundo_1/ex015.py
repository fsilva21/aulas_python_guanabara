#Escreva um programa que pergunte a quantidade de Km percorridos e a quantidade de dias que foi alugado. Calcule o preço a pagar, sabendo que o carro custa:
#Carro:R$60 por dia. Km rodado: R$0.15

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km rodados? '))
preco_dias = dias*60
preco_km = km*0.15


print(f'{dias} dias rodados: R${preco_dias}\n{km} Km rodados: R${preco_km:.2f}\nTotal a pagar: R${preco_km + preco_dias:.2f}')