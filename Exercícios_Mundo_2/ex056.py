#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#  >A média de idade do grupo - OK
#  >Qual é o nome do homem mais velho - OK
#  >Quantas mulheres tem menos de 20 anos - OK

total_idade = 0
maior_idade = 0
total_mulheres = 0
for c in range(0,4):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: Digite (M) para masculino ou (F) para feminino: ')).upper()
    total_idade += idade
    if c == 0:
        maior_idade = idade
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_do_velho = nome
    if idade < 20 and sexo == 'F':
        total_mulheres += 1
print(f'A média de idade do grupo é de {total_idade / 4}')
print(f'O homem mais velho é {nome_do_velho} com {maior_idade} anos')
print(f'Neste grupo, há {total_mulheres} mulheres com menos de 20 anos')