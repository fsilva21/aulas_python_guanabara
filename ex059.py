#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso

print('Bem vindo(a)')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('Entre com a operação desejada:\n'
                     '                     [1] SOMAR\n'
                     '                     [2] MULTIPLICAR\n'
                     '                     [3] MAIOR VALOR\n'
                     '                     [4] NOVOS NÚMEROS\n'
                     '                     [5] SAIR\n'
                     '        '))
    if menu == 1:
        print(f'A soma dos entre {num1} e {num2} é de: {num1 + num2}')
    elif menu == 2:
        print(f'A multiplicação de {num1} por {num2} é de {num1 * num2}')
    elif menu == 3:
        if num1 > num2: print(f'O maior valor é {num1}')
        elif num2 > num1: print(f'O maior valor é {num2}')
        else: print('Os números são iguais!')
    elif menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif menu > 5 or menu < 0:
        print('Por favor, digite um número válido.')