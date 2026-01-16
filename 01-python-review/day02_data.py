lista_nomes = ['Renan', 'Caio', 'Vitor', 'Joao', 'Matheus']
lista_idades = [20, 30, 30, 12, 17]

#EXC 1
for indice, nome in enumerate(lista_nomes, start=1):
    print(f'{indice} - {nome}')

#EXC 2
for nome, idade in zip(lista_nomes, lista_idades):
    print(f'{nome} tem {idade} anos.')

#EXC 3
lista_txt_nomes = []

with open('01-python-review/data/nomes.txt', 'r') as nomes:
    for n in nomes:
        lista_txt_nomes.append(n.upper().strip())

print(lista_txt_nomes)

#EXC 4
with open('01-python-review/data/pessoas.txt', 'r') as pessoas:
    lista_pessoas = []
    lista_atualizada = []
    for pessoa in pessoas:
        lista_pessoas.append(pessoa.strip().split(','))

    for pessoa in lista_pessoas:
        pessoa[1] = int(pessoa[1])

    for pessoa in lista_pessoas:
        if pessoa[1] >= 18:
            dicionario_pessoas = dict({'nome': pessoa[0], 'idade': pessoa[1]})
            lista_atualizada.append(dicionario_pessoas)

    print(lista_atualizada)