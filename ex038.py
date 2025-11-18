#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens:
#> O primeiro valor é maior;
#> O segundo valor é maior;
#> Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite um número novamente: '))
if num1 > num2:
    print(f'O primeiro valor é maior ({num1})')
elif num2 > num1:
    print(f'O segundo valor é maior ({num2})')
else:
    print(f'Os valores são iguais ({num1},{num2})')
