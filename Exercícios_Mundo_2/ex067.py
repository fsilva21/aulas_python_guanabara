#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
#O programa será interrompido quando o número solicitado for negativo

print('*'*10,'Programa de Tabuada','*'*10)
while True:
    num = int(input('Digite um número positivo (negativo para sair): '))
    if num < 0:
        print('-'*10,'Fim do programa','-'*10)
        break
    print(f'{'*'*5} TABUADA DO NÚMERO {num} {'*'*5}')
    for c in range(1,11):
        print(f'{c} x {num} = {c * num}')
