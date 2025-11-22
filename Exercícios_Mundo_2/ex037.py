#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
#-1 para binário −2 para octal -3 para hexadecimal

num = int(input('Digite um numero inteiro: '))
opcao = int(input('Escolha uma opção de conversão: \n1 - Binário\n2 - Octal \n3 - Hexadecimal\nOpção desejada: '))
if opcao == 1:
    print(f'O número {num} convertido para binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Opção Inválida!\nPrograma Encerrado')