# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão, na ordem de colocação, depois mostre:
# - Apenas os 5 primeiros colocados
# - Os últimos 4 colocados na tabela
# - Uma lista com os times em ordem alfabética
# - Em que posição na tabela está o time do Mirassol

times = ("Palmeiras", "Flamengo", "Cruzeiro", "Mirassol", "Bahia", "Botafogo",
"Fluminense", "São Paulo", "Vasco da Gama", "Corinthians", "Bragantino", "Atlético Mineiro",
"Grêmio", "Ceará", "Internacional", "Santos", "Vitória", "Fortaleza", "Juventude", "Sport")

contador = 1
print(f'''Tabela dos times em ordem alfabética: {sorted(times)}
{'=*'*20}''')
print(f'Primeiros 5 colocados: {times[0:5]}\n{'=*'*20}')
print(f'Últimos 4 colocados: {times[-4:]}\n{'=*'*20}')
for c in times:
    if c == 'Mirassol':
        print(f'O time do {c} se encontra na {contador}ª posição!')
        break
    contador += 1

#print(f'O time do Mirassol se encontra na {times.index('Mirassol')+1}ª posição!')