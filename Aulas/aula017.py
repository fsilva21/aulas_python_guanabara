# AULA SOBRE LISTAS (PARTE 1)

lista = ['hambúrguer','pizza']

lista.append('cachorro quente') # Adiciona um item no final da lista
del lista[2] # Deleta um item da lista
lista.pop(1) # Pode ser usado pra eliminar o último elemento. Se usado com o parâmetro, pode-se escolher o item
lista.remove('pizza') # Igual ao pop, porém ao invés do índice, especifica-se o nome do item
if 'pizza' in lista:
    lista.remove('pizza')

valores = list(range(4,11)) # Cria uma lista de 4 até 10

valor = [8,2,5,4,9,3,0] # Lista fora de ordem
valor.sort() # Organiza a lista em ordem crescente
valor.sort(reverse=True) # Organiza em ordem reversa