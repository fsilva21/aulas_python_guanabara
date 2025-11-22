# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar

from datetime import date

ano_atual = date.today().year
cadastro = {'nome': str(input('Nome: ')), 'idade': (int(input('Ano de Nascimento: ')) - ano_atual) * -1, 'ctps': int(input('Carteira de Trabalho ([0] não tem): '))}
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = 30 - (ano_atual - cadastro['contratação']) + cadastro['idade']
print('*-'*15)
for k, v in cadastro.items():
    print(f'{k}: {v}')