# Crie um programa que tenha uma função chamada "voto()" que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando uma frase (string).
# Essa string indicará se a pessoa tem o voto NÃO VOTA, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    print(f'Com {idade} anos: ',end='')
    if 65 > idade >= 18:
        return 'VOTO OBRIGATÓRIO.'
    elif 18 > idade >= 16 or idade > 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'NÃO VOTA.'


print(voto(2008))