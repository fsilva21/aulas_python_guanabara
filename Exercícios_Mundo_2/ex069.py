#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# - Quantas pessoas tem mais de 18 anos
# - Quantos homens foram cadastrados
# - Quantas mulheres tem menos de 20 anos

maior = homens = mulheres_ate_20 = 0
while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo in 'MF':
            break
        else:
            print('Digite uma opção válida, tente novamente.')
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_ate_20 += 1
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Foram cadastradas {maior} pessoas acima de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres_ate_20} mulheres de até 20 anos.')