#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

condicao = soma = contador = 0
while condicao != 999:
    num = int(input('Digite um número qualquer ("999" para sair): '))
    if num == 999:
        condicao = 999
        num = 0
    else:
        soma += num
        contador += 1
print(f'Fora digitados {contador} números, e a soma entre eles é de {soma}')