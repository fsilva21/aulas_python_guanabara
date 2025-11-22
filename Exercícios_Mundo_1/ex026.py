#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count('a')} vezes')
print('A letra "a" aparece pela primeira vez na posição:', frase.find('a'))
print('E pela última vez na posição: ', frase.rfind('a'))