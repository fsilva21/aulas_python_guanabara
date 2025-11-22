# Crie um programa que vai ler vários números e colocar em uma lista. Depois, crie duas listas extras que vão conter valores pares e ímpares, respectivamente.
# No final, mostre o conteúdo das 3 listas geradas

valores = []
lista_par = []
lista_impar = []
while True:
    valores.append(int(input('Digite um número: ')))
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if pergunta == 'N':
        break
for i in valores:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')