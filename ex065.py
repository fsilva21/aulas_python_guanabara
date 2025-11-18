#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

condicao = maior = menor = contador = soma = 0
while condicao == 0:
    num = int(input('Digite um número: '))
    soma += num
    if contador == 0:
        maior = num
        menor = num
    elif contador > 0:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    contador += 1
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if resposta == "N":
        condicao = 1
media = (soma / contador)
print(f'A média dos valores fornecidos é de {media:.2f}')
print(f'Maior valor: {maior}\nMenor valor: {menor}')