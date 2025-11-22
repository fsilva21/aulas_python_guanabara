#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000

print(f'O valor digitado foi {m:.2f}m\nValor em centímetros: {cm:.0f}cm\nValor em milímetros: {mm:.0f}mm')