# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

aluno = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if aluno['Média'] >= 5:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
aluno['Situação'] = situacao
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
