'''
with open('01-python-review/data/pessoas.txt', 'r') as pessoas:
    lista_pessoas = []
    for pessoa in pessoas:
        lista_pessoas.append(pessoa.strip().split(','))

    for pessoa in lista_pessoas:
        pessoa[1] = int(pessoa[1])

    lista_atualizada = []

    for pessoa in lista_pessoas:
        if pessoa[1] > 18:
            dicionario_pessoas = dict({'nome': pessoa[0], 'idade': pessoa[1]})
            lista_atualizada.append(dicionario_pessoas)

    print(lista_atualizada)
'''

#* Uso de LIST COMPREHENSION
'''
with open('01-python-review/data/pessoas.txt', 'r') as pessoas:
    lista_pessoas = []
    for pessoa in pessoas:
        lista_pessoas.append(pessoa.strip().split(','))

    for pessoa in lista_pessoas:
        pessoa[1] = int(pessoa[1])

    lista_atualizada = [
        {'nome': pessoa[0], 'idade': pessoa[1]}
        for pessoa in lista_pessoas
        if pessoa[1] > 18
    ]

    print(lista_atualizada)
'''
#* Exercício final DIA 3 (LIST COMPREHENSION)

pessoas = [
    ['Ana', 17],
    ['Bruno', 22],
    ['Carlos', 18],
    ['Diana', 16]
]

pessoas_atualizadas = [
    {'nome': pessoa[0], 'idade': pessoa[1]}
    for pessoa in pessoas if pessoa[1] >= 18
]

print(pessoas_atualizadas)



