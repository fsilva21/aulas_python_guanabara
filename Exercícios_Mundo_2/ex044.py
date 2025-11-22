#Elabore um programa que calcula o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
#  >À vista dinheiro/cheque: 10% de desconto
#  >À vista no cartão: 5% de desconto
#  >Em até 2x no cartão: preço normal
#  >3x ou mais no cartão: 20% de juros

print(f'{' LOJAS TABAJARA ':=^40}')
preco = float(input('Qual o valor do produto? R$ '))
opcao = int(input('Selecione uma opção de pagamento:\n(1) À vista dinheiro/cheque - 10% desconto\n(2) À vista no cartão - 5% desconto\n(3) Em até 2x no cartão - Valor normal\n(4) 3x ou mais no cartão - 20% de juros\nOpção escolhida: '))
print(f'Valor do produto: R$ {preco:.2f}')
if opcao == 1:
    preco = preco - (preco * 0.1)
    print(f'Novo valor, com 10% de desconto: R$ {preco:.2f}')
elif opcao == 2:
    preco = preco - (preco * 0.05)
    print(f'Novo valor, com 5% de desconto: R$ {preco:.2f}')
elif opcao == 3:
    print(f'Valor final R$ {preco:.2f}\n(2) Parcelas de R$ {preco / 2:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?: '))
    preco = preco + (preco * 0.2)
    print(f'Valor do produto com 20% de juros: R$ {preco:.2f}\nForma de pagamento: {parcelas} parcelas de R$ {preco / parcelas:.2f}')
else:
    print('Por favor digite uma opção válida')