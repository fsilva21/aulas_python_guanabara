# pessoas = {'Nome': 'Gustavo','Sexo': 'M', 'Idade': 22}
# pessoas['Peso'] = 98.5
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for dic in brasil:
    for k, v in dic.items():
        print(f'O campo {k} tem valor {v}')
