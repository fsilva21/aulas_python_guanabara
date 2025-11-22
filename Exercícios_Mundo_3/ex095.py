# Aprimore o desafio 093 para que ele funciona com vários jogadores, incluindo com um sistema de visualização de detalhes do aproveitamento de cada jogador


cadastro = []
while True:
    total = 0
    gols = []
    jogador = {'nome': str(input('Nome do jogador: ')), 'gols': gols}
    partidas = int(input(f'Partidas que {jogador['nome']} jogou: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c +1}? ')))
        total += gols[c]
    jogador['total'] = total
    cadastro.append(jogador.copy())
    jogador.clear()
    pergunta = str(input('Quer continuar [S/N]? ')).upper().strip()
    if pergunta == 'N':
        break
    print('--'*20)
print('*-'*30)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<15}{"TOTAL":>5}')
print('--'*30)
for pos, dicionarios in enumerate(cadastro):
    print(f'{pos:<5}{dicionarios['nome']:<15}{str(dicionarios['gols']):<15}{dicionarios['total']:>5}')
while True:
    print('--' * 30)
    escolha = int(input('Digite o código do jogador para ver suas estatísticas (999 para sair):  '))
    if escolha == 999:
        break
    if escolha >= len(cadastro) or escolha < 0:
        print(f'ERRO! Não existe jogador com o código {escolha}. Tente novamente.')
    for pos, dicionarios in enumerate(cadastro):
        if escolha == pos:
            print(f'-- Levantamento do jogador {dicionarios['nome']}:')
            for jogo, gol in enumerate(dicionarios['gols']):
                print(f'{" ":<4}No jogo {jogo+1} fez {gol} gol(s)')
            print(f'Foi um total de {dicionarios['total']} gols, com uma média de {sum(dicionarios['gols']) / len(dicionarios['gols']):.2f} gols por jogo.')
print(f'{"PROGRAMA FINALIZADO":-^15}')
