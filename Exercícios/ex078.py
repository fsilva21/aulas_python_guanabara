# Faça um programa que leia 5 valores numéricos e guarde numa lista.
# No final mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista

valores = []
maior = menor = 0
for val in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if val == 0:
        maior = valores[0]
        menor = valores[0]
for pos, val in enumerate(valores):
    if val > maior:
        maior = val
        pos_maior = pos
    if val <= menor:
        menor = val
        pos_menor = pos
print(f'O maior valor é {maior} na {pos_maior + 1}ª posição')
print(f'O menor valor é {menor} na {pos_menor + 1}ª posição')

# VERSÃO OTIMIZADA GPT
# valores = [int(input('Digite um valor: ')) for _ in range(5)]
# maior = max(valores)
# menor = min(valores)
# print(f'O maior valor é {maior} na {valores.index(maior) + 1}ª posição')
# print(f'O menor valor é {menor} na {valores.index(menor) + 1}ª posição')
