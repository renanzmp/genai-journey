lista_numeros = [1, 4, 6, 7, 10]

for n in lista_numeros:
    if n%2 == 0:
        print(f'O número {n} é par')
    else:
        print(f'O número {n} é impar')
    

lista_numeros_diferentes = [4, -2, 7, 9, -1, 3, -4, 8]

for n in lista_numeros_diferentes:
    if n >= 0:
        print(f'O número {n} é positivo')
    else:
        print(f'O número {n} é negativo')


def processar_lista(lista):
    lista_positivos = []
    for n in lista:
        if n >= 0:
            lista_positivos.append(n)
    lista_atualizada = []
    if lista_positivos != []:
        maior_numero = max(lista_positivos)
        for n in lista_positivos:
            lista_atualizada.append(n/maior_numero)
    else:
        return lista_atualizada

    return lista_atualizada

resultado = processar_lista(lista_numeros_diferentes)

print(resultado)