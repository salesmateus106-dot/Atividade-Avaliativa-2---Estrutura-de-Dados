# PARTE 6 – ANÁLISE E CONCLUSÃO

## Tabelas de operações

### Ordenação (Bubble Sort x Quick Sort)

Valores de uma execução. Como os dados são gerados aleatoriamente, as trocas e o tempo
variam a cada rodada (as comparações do Bubble são fixas pelo tamanho da lista).

| Tamanho | Algoritmo   | Comparações | Trocas/Movimentações | Tempo (s) |
|---|---|---|---|---|
| 10   | Bubble Sort | 90     | 29     | 0.000009 |
| 10   | Quick Sort  | 23     | 23     | 0.000016 |
| 20   | Bubble Sort | 380    | 112    | 0.000026 |
| 20   | Quick Sort  | 69     | 69     | 0.000013 |
| 1000 | Bubble Sort | 999000 | 246914 | 0.056232 |
| 1000 | Quick Sort  | 12626  | 12626  | 0.001002 |

### Busca sequencial em matrizes

Comparações conforme a posição do valor procurado (valores estáveis, pois a matriz é
preenchida em ordem).

| Matriz  | Elementos | Início | Final | Inexistente |
|---|---|---|---|---|
| 2x2     | 4     | 1 | 4     | 4     |
| 10x10   | 100   | 1 | 100   | 100   |
| 100x100 | 10000 | 1 | 10000 | 10000 |

## 1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?

Sim. Nos testes, quanto maior a lista, mais operações os dois algoritmos precisaram fazer. No Bubble Sort, as comparações saíram de 90 (com 10 elementos) para 999.000 (com 1.000). No Quick Sort, foram de 23 para 12.626. Ou seja, o tamanho da entrada influencia diretamente: quanto mais dados, mais trabalho o algoritmo faz para ordenar. O mesmo acontece na busca em matrizes, já que uma matriz maior tem mais posições para percorrer, então o número de comparações também aumenta.

## 2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?

Não. Os dois crescem em ritmos bem diferentes. O Bubble Sort cresce muito mais rápido, porque seu comportamento é O(n²): quando o número de elementos aumenta, a quantidade de operações dispara. O Quick Sort cresce bem mais devagar, com comportamento O(n log n) em média. Dá para ver isso nos números: com 10 elementos a diferença é pequena (90 contra 23 comparações), mas com 1.000 ela fica enorme (999.000 contra 12.626). No tempo acontece o mesmo: o Bubble levou 0,056 segundos e o Quick apenas 0,001. Isso mostra que eles não escalam do mesmo jeito.

## 3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?

Porque os dois algoritmos chegam exatamente no mesmo resultado: a lista fica ordenada igual, não importa qual foi usado. Se olharmos só a saída, não dá para dizer qual é melhor, porque as duas parecem iguais. O que realmente diferencia um algoritmo do outro é o custo do processo, ou seja, quantas comparações e trocas ele fez e quanto tempo levou para chegar lá. Por isso a gente conta as operações: é a eficiência (o "como" ele ordena) que separa um algoritmo bom de um ruim, e não o resultado final.

## CONCLUSÃO

Os experimentos mostraram que o tamanho da entrada afeta diretamente a quantidade de operações, e que Bubble Sort e Quick Sort não crescem da mesma forma: o Bubble fica cada vez mais lento conforme os dados aumentam, enquanto o Quick se mantém eficiente mesmo com muitos elementos. Também ficou claro que olhar apenas o resultado final não é suficiente para comparar algoritmos, já que os dois ordenam igual, sendo preciso medir o processo. Por isso, o Quick Sort é a melhor escolha para grandes volumes de dados, e o Bubble Sort só compensa em listas pequenas ou quase ordenadas.
