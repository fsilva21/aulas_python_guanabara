#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Se estiver errado, peça novamente até obter um valor correto

sexo = str
while sexo != "M" and sexo != "F":
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if sexo != "M" and sexo != "F":
        print('Digite uma opção válida')
if sexo == "M":
    print('Você é uma pessoa do sexo masculino')
else:
    print('Você é uma pessoa do sexo feminino')