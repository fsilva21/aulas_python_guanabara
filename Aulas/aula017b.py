"""num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(0,2) # Insere o valor '0' na posição '2'
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')"""

'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for contador, valores in enumerate(valores):
    print(f'O {contador + 1}º valor é {valores}')'''

a = [2,3,4,7]
#b = a # Cria uma ligação, onde se mexer em uma lista, a outra também é alterada
b = a[:] # Cria uma cópia, onde 'b' pode ser mexida livremente sem alterar 'a'
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')