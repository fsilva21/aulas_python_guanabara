#Escreva um programa que pergunte o salário de um funcionário e calcule o aumento
#Salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Menor ou igual a este valor, 15% de aumento

salario = float(input('Qual seu salário atual? R$ '))
if salario > 1250:
    print(f'Novo salário com reajuste de 10%:\nR$ {salario + (salario * 0.1)}')
else:
    print(f'Novo salário com reajuste de 15%:\nR$ {salario + (salario * 0.15)}')