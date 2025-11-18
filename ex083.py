# Crie um programa onde o usuário digite uma expressão '((a+b)*c)' qualquer que use parênteses.
# Seu programa deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta

expressao = input('Digite sua expressão: ')
valores = []
cont_parenteses = 0
for i in expressao:
    valores.append(i)
for c in valores:
    if c == '(':
        cont_parenteses += 1
    elif c == ')':
        cont_parenteses -= 1
        if cont_parenteses < 0:
            break
if cont_parenteses == 0:
    print(f'A expressão está correta!')
else:
    print(f'A expressão está errada!')