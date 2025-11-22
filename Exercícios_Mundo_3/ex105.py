# Faça um programa que tenha uma função "notas()" que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as DOCSTRINGS da função

def notas(* n, sit=False):
    """

    :param n: Insira as notas da turma
    :param sit: Caso deseje ver a situação: sit=True
    :return: Retorna o dicionário com os dados da turma e a situação caso solicitado
    """
    media = sum(n) / len(n)
    dicio = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': f'{media:.2f}'}
    if sit:
        if media >= 7:
            dicio['situação'] = 'BOA'
        elif media < 5:
            dicio['situação'] = 'RUIM'
        else:
            dicio['situação'] = 'RECUPERAÇÃO'
    return dicio


resp = notas(7.5,7,8.5, sit=True)
help(notas)