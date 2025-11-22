# Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla. No final mostre:
# - Quantas vezes apareceu o valor 9
# - Em que posição foi digitado o primeiro valor 3
# - Quais foram os números pares

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1,num2,num3,num4)
print(f'Os valores armazenados foram: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição ')
else:
    print('O valor 3 não consta no sistema')
print(f'Os seguintes valores pares foram digitados: ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')