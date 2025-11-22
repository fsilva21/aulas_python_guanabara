#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais termos. O programa encerra quando ele disser que quer mostrar 0 termos

termo = int(input('Primeiro termo da PA: '))
while termo != 0:
    contador = 0
    razao = int(input('Razão: '))
    while contador != 10:
        print(termo, end=' ')
        termo += razao
        contador += 1
    termo = int(input('\nDeseja fazer outra consulta?\nDigite o número desejado ou [0] para sair: '))

