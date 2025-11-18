#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input('Qual sua cidade? ')).strip()
cidade_tratada = cidade.lower()
print('santo' in cidade_tratada[:5])
