# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final:
# Mostre um boletim contendo média de cada um
# Permita que o usuário possa mostrar a nota de cada aluno individualmente.

alunos = list()
nomes = []
notas = []
num = 0
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()
    pergunta = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while pergunta not in 'SN':
        pergunta = str(input('Opção inválida.\nDeseja continuar [S/N]?')).upper().strip()
    if pergunta == 'N':
        break
print('*-'*30)
print(f'{'Nº': <5}{'NOME':<15}{'MÉDIA':<10}')
print('-'*25)
for pos, c in enumerate(alunos):
    print(f'{pos: <5}{c[0]: <15}{(c[1][0] + c[1][1]) / 2:.2f}')
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        print('ENCERRANDO PROGRAMA...')
        print('*-'*15)
        break
    for pos, c in enumerate(alunos):
        if num == pos:
            print(f'Notas de {c[0]} são: {c[1]}')
            print('*-'*15)
            break
    else:
        print('Aluno não encontrado')