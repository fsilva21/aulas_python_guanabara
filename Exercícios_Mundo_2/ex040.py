#Crie um programa que calcule a média, e mostre uma das mensagens:
#  >Média abaixo de 5.0: REPROVADO
#  >Média entre 5.0 e 6.9: RECUPERAÇÃO
#  >Média 7.0 ou superior: APROVADO

print('Calculador de médias\nPor favor, digite 3 notas')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print(f'Sua média é {media:.1f}')
if media < 5:
    print('Situação: REPROVADO')
elif 7 > media >= 5:
    print('Situação: RECUPERAÇÃO')
else:
    print('Situação: APROVADO')