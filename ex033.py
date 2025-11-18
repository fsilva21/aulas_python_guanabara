#Faça um programa que leia 3 números e mostre qual é o maior e qual o menor

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
if num1 > num2 and num1 > num3:
    maior = int(num1)
elif num2 > num1 and num2 > num3:
    maior = int(num2)
else:
    maior = int(num3)

if num1 < num2 and num1 < num3:
    menor = int(num1)
elif num2 < num1 and num2 < num3:
    menor = int(num2)
else:
    menor = int(num3)
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')