import random
import time


def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(n - 1):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, comparacoes, trocas


def quick_sort(lista):
    if len(lista) <= 1:
        return lista, 0, 0

    pivo = lista[0]

    menores = []
    maiores = []

    comparacoes = 0
    movimentacoes = 0

    for numero in lista[1:]:
        comparacoes += 1

        if numero <= pivo:
            menores.append(numero)
            movimentacoes += 1
        else:
            maiores.append(numero)
            movimentacoes += 1

    menores_ordenados, comp_menores, mov_menores = quick_sort(menores)
    maiores_ordenados, comp_maiores, mov_maiores = quick_sort(maiores)

    comparacoes += comp_menores + comp_maiores
    movimentacoes += mov_menores + mov_maiores

    lista_ordenada = menores_ordenados + [pivo] + maiores_ordenados

    return lista_ordenada, comparacoes, movimentacoes

quantidades = [10, 20, 1000]

for quantidade in quantidades:

    lista = []

    for i in range(quantidade):
        numero = random.randint(1, 10000)
        lista.append(numero)

    print("\nQuantidade de números:", quantidade)

    # -------------------------
    # BUBBLE SORT
    # -------------------------

    lista_bubble = lista.copy()

    inicio = time.perf_counter()

    lista_bubble, comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

    fim = time.perf_counter()

    tempo_bubble = round (fim - inicio, 10)

    print("\nBubble Sort:")
    print(lista_bubble)
    print("Comparações:", comparacoes_bubble)
    print("Trocas:", trocas_bubble)
    print("Tempo:", tempo_bubble, "segundos")


    # -------------------------
    # QUICK SORT
    # -------------------------

    lista_quick = lista.copy()

    inicio = time.perf_counter()

    lista_quick, comparacoes_quick, movimentacoes_quick = quick_sort(lista_quick)

    fim = time.perf_counter()

    tempo_quick = round(fim - inicio, 10)

    print("\nQuick Sort:")
    print(lista_quick)
    print("Comparações:", comparacoes_quick)
    print("Movimentações:", movimentacoes_quick)
    print("Tempo:", tempo_quick, "segundos")


"""

a)Qual algoritmo realizou menos operações para 10 elementos?
O Quick Sort.

b) O comportamento permaneceu igual para 20 elementos?
Sim.

c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?
Realizou mais operações.

d) Qual algoritmo apresentou maior crescimento da quantidade de operações?
O Bubble Sort.

e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?
Sim.

f) Em qual situação você escolheria Bubble Sort?
Em um algoritmo que possa ser interrompido e retomado a qualquer momento sem perder o progresso.

g) Em qual situação você escolheria Quick Sort?
Quando ordenasse grandes volumes de dados no menor tempo possível, sem restrições severas de memória RAM.

"""