#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o ultimo nome separadamente
#Ex: Ana Maria de Souza Primeiro:Ana Ultimo:Souza

nome = str(input('Digite o nome completo: ')).strip().split()
print(f'Seu primeiro nome é {nome[0]}\nSeu último nome é {nome.pop()}')