#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite seu salário atual: '))
reajuste = salario + (salario * 0.15)
print(f'Seu salário atual é de R${salario}\nNovo valor com 15% de aumento: R${reajuste:.2f}')