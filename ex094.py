# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final mostre:
# - Quantos pessoas foram cadastradas
# - A média de idade do grupo
# - Uma lista com todas as mulheres
# - Uma lista com todas as pessoas com idade acima da média

cadastro = []
media = 0
while True:
    pessoa = {'nome': str(input('Nome: ')), 'sexo': str(input('Sexo: [M/F] ')), 'idade': int(input('Idade: '))}
    media += pessoa['idade']
    cadastro.append(pessoa.copy())
    pessoa.clear()
    pergunta = str(input('Quer continuar [S/N]? ')).upper().strip()
    if pergunta == 'N':
        break
print(cadastro)
print(f'- O grupo tem {len(cadastro)} pessoas.')
media = media / len(cadastro)
print(f'- A média de idade é de {media:.2f}')
print(f'- As mulheres cadastradas foram: ',end='')
for dicionarios in cadastro:
    if dicionarios['sexo'] in 'fF':
        mulher = dicionarios['nome']
        print(mulher,end=' ')
print(f'\n- Lista de pessoas que estão acima da média de idade: ')
for dicionarios in cadastro:
    if dicionarios['idade'] > media:
        print()
        for k, v in dicionarios.items():
            print(f'{k}: {v}',end='; ')