#Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
#O programa deverá informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

cedulas_de_20 = cedulas_de_10 = 0
valor = int(input('Valor do saque: R$'))
unidade = valor // 1 % 10
dezena = (valor // 10 % 10) * 10
centena = (valor // 100 % 10) * 100
milhar = (valor // 1000 % 10) * 1000
cedulas_de_50 = (centena + milhar) // 50
if dezena // 50 == 1:
    cedulas_de_50 += 1
    dezena -= 50
if dezena // 20 == 1:
    cedulas_de_20 += 1
    dezena -= 20
elif dezena // 20 == 2:
    cedulas_de_20 += 2
    dezena -= 40
if dezena // 10 == 1:
    cedulas_de_10 += 1
    dezena -= 10
print(f'''Cédulas:
{cedulas_de_50} notas de R$50
{cedulas_de_20} notas de R$20
{cedulas_de_10} notas de R$10
{unidade} notas de R$1
''')
