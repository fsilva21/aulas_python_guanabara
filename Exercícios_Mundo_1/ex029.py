#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por KM acima do limite

velocidade_carro = int(input('Qual a velocidade atual do carro? '))
if velocidade_carro > 80:
    velocidade_carro = (velocidade_carro - 80) * 7
    print(f'Você ultrapassou o limite de velocidade e terá que pagar uma multa de R${velocidade_carro}')
else:
    print('Você está dentro do limite de velocidade')