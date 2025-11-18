#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: A TORRE DA DERROTA

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palindromo!')