#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas
#-O nome com todas as letras minúsculas
#-Quantas letras ao todo, sem considerar os espaços
#-Quantas letras tem o primeiro nome

nome = input('Nome completo: ')
print(nome.upper())
print(nome.lower())
nome_split = nome.split()
print(nome_split)
print(f'Seu nome tem {len(''.join(nome_split))} letras')
print(f'Seu primeiro nome é {nome_split[0]}, que possui {len(nome_split[0])} letras')