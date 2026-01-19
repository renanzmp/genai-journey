'''
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
'''

with open('01-python-review/data/pessoas.txt', 'r') as pessoas:
    lista_pessoas = []
    lista_atualizada = []
    for pessoa in pessoas:
        lista_pessoas.append(pessoa.strip().split(','))

    for pessoa in lista_pessoas:
        pessoa[1] = int(pessoa[1])

    lista_atualizada = []

    for pessoa in lista_pessoas:
        if pessoa[1] >= 18:
            dicionario_pessoas = dict({'nome': pessoa[0], 'idade': pessoa[1]})
            lista_atualizada.append(dicionario_pessoas)

    print(lista_atualizada)