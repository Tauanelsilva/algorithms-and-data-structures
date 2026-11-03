# Algoritmos e estruturas de dados

Implementações curtas, com o custo anotado e teste automático. Servem para eu revisar a matéria e mostrar a versão que eu consigo explicar.

## Python

| Peça | Arquivo | Custo que eu assumo |
| --- | --- | --- |
| Merge sort | `python/algorithms/sorting.py` | O(n log n) tempo, O(n) memória extra |
| Busca binária | `python/algorithms/search.py` | O(log n), lista já ordenada |
| BFS | `python/algorithms/graphs.py` | O(V + A) |
| Dijkstra | `python/algorithms/graphs.py` | O((V + A) log V), pesos não negativos |
| Pilha, fila e hash com encadeamento | `python/algorithms/structures.py` | push/pop O(1); get/put O(1) no caso médio |

A fila em lista usa `pop(0)`, então o `dequeue` desta versão é O(n). Deixei assim de propósito: a versão didática fica visível, e o comentário no README evita vender complexidade errada.

## Rodar os testes

```bash
python -m pip install pytest
pytest
```

## C++

`cpp/main.cpp` repete merge sort e busca binária. O `main` confere os resultados com `assert`.

```bash
g++ -std=c++17 cpp/main.cpp -o cpp/algoritmos
./cpp/algoritmos
```

No Windows, o executável sai como `cpp\algoritmos.exe` se o compilador estiver no PATH.
