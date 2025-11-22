#Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar:
#≥ Valor da casa ≥ Salário do comprador ≥ Em quantos anos ele pretende pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('Solicite seu empréstimo')
valor_casa = float(input('Valor do imóvel: R$ '))
salario = float(input('Valor do seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar?: '))
parcelas = valor_casa / (anos * 12)
print(f'Seu financiamento é de {anos*12} parcelas de R$ {parcelas:.2f}')
if parcelas > (salario * 0.3):
    print('Desculpe, seu empréstimo foi negado')
else:
    print(f'Seu empréstimo foi APROVADO!')