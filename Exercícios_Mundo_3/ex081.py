# Crie um programa que vai ler vários números e colocar em uma lista, depois mostre:
# -Quantos números foram digitados
# -A lista de valores, ordenada de forma decrescente
# -Se o valor 5 foi digitado e está ou não na lista

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if pergunta in 'SN':
            break
        else:
            print('Entre com uma opção válida.')
    if pergunta == 'N':
        break
print(f'Foram lidos {len(valores)} valores')
valores.sort(reverse=True)
print(valores)
for pos, i in enumerate(valores):
    if i == 5:
        print(f'O valor 5 foi encontrado na posição {pos}')
        break
else:
    print('Não há o número 5 na lista')