# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 2, 'Caneta', 3.50, 'Caderno', 13.90, 'Borracha', 0.75, 'Apontador', 3, 'Pasta', 7, 'Mochila', 114.90)
contador = 0
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)
for lista in produtos:
    if contador % 2 == 0:
        print(f'{lista:.<20}',end=' ')
    else:
        print(f'R$ {lista:.2f}')
    contador += 1
print('-' * 50)