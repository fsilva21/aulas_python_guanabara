#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#  >Se ele ainda vai se alistar
#  >Se é a hora de se alistar
#  >Se já passou do tempo de alistamento
#O programa deve mostrar o tempo que falta ou que passou do prazo

from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano_alistamento = date.today().year - 18
print(f'Você está com {(ano_nascimento - date.today().year) * - 1} anos')
sexo = str(input('Qual seu sexo? Digite (M) masculino ou (F) feminino: '))
if sexo == 'M' or sexo == 'm':
    if ano_nascimento > ano_alistamento:
        print(f'Ainda faltam {ano_nascimento - ano_alistamento} ano(s) para você se alistar')
    elif ano_nascimento < ano_alistamento:
        print(f'Já se passaram {ano_alistamento - ano_nascimento} ano(s) do seu alistamento obrigatório')
    else:
        print(f'Você tem 18 anos e pode se alistar')
elif sexo == 'F' or sexo == 'f':
    print('Você é do sexo feminino, portanto não é necessário se alistar')
else:
    print('Por favor, digite uma opção válida')