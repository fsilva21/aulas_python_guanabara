# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista. Caso o número já exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[len(valores)-1] in valores[0:len(valores)-2]:
        del valores[len(valores)-1]
        print('Valores duplicados não são permitidos.')
    while True:
        pergunta = str(input('Quer continuar [S/N]? ')).strip().upper()
        if pergunta in 'SN':
            break
        else:
            print('Digite uma opção válida...Tente novamente')
    if pergunta == 'N':
        break
valores.sort()
print(valores)

"""VERSÃO REFATORADA GPT"""

# valores = []
#
# while True:
#     valor = int(input('Digite um valor: '))
#     if valor not in valores:
#         valores.append(valor)
#         print('Valor adicionado com sucesso!')
#     else:
#         print('Valor duplicado! Não será adicionado.')
#     pergunta = input('Quer continuar [S/N]? ').strip().upper()
#     while pergunta not in ('S', 'N'):
#         pergunta = input('Digite uma opção válida [S/N]: ').strip().upper()
#     if pergunta == 'N':
#         break
# valores.sort()
# print(f'\nVocê digitou os valores: {valores}')
