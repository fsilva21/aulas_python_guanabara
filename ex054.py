#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

lista_pessoas_maiores = []
lista_pessoas_menores = []
for c in range(0,7,1):
    nome = str(input(f'Digite o nome da {c+1}ª pessoa: '))
    ano_nascimento = int(input('Insira o ano que nasceu: '))
    ano_nascimento = (date.today().year - ano_nascimento)
    pessoa = {'Nome':nome,'Idade':ano_nascimento}
    if ano_nascimento >= 21:
        lista_pessoas_maiores.append(pessoa)
    elif ano_nascimento < 21:
        lista_pessoas_menores.append(pessoa)
print('*-'*5,' LISTA DE PESSOAS MAIORES DE IDADE ','-*'*5)
for pessoa in lista_pessoas_maiores:
    print(f'Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}')
print('*-'*5, ' LISTA DE PESSOAS MENORES DE IDADE ', '-*'*5)
for pessoa in lista_pessoas_menores:
    print(f'Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}')
