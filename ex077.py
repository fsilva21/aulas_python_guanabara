# Crie um programa que tenha uma tupla com várias palavras (sem usar acentos). Depois, você deve mostrar, para cada palavra, quais são suas vogais

times = ("Palmeiras", "Flamengo", "Cruzeiro", "Mirassol", "Bahia", "Botafogo",
"Fluminense", "Sao Paulo", "Vasco da Gama", "Corinthians", "Bragantino", "Atletico Mineiro",
"Gremio", "Ceara", "Internacional", "Santos", "Vitoria", "Fortaleza", "Juventude", "Sport")

for letras in times:
    print(f'\nNa palavra {letras} temos ',end='')
    for c in letras:
        if c.lower() in 'aeiou':
            print(c.lower(),end=' ')
