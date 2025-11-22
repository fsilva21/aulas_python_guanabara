#Leia o nascimento de um atleta de natação e mostre sua categoria, de acordo com sua idade:
#  >Até 9 anos: MIRIM
#  >Até 14 anos: INFANTIL
#  >Até 19 anos: JUNIOR
#  >Até 25 anos: SÊNIOR
#  >Acima:      MASTER

import datetime
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - ano_nascimento
print(f'Idade: {idade} anos')
if idade < 9:
    print(f'Categoria: MIRIM')
elif 9 <= idade < 14:
    print(f'Categoria: INFANTIL')
elif 14 <= idade < 19:
    print('Categoria: JUNIOR')
elif 19 <= idade < 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')