class Stack:
    def __init__(self) -> None:
        self._items: list[object] = []

    def push(self, item: object) -> None:
        self._items.append(item)

    def pop(self) -> object:
        if not self._items:
            raise IndexError("pilha vazia")
        return self._items.pop()


class Queue:
    def __init__(self) -> None:
        self._items: list[object] = []

    def enqueue(self, item: object) -> None:
        self._items.append(item)

    def dequeue(self) -> object:
        if not self._items:
            raise IndexError("fila vazia")
        return self._items.pop(0)


class HashMap:
    """Tabela hash com encadeamento. O custo médio de get e put é O(1)."""

    def __init__(self, buckets: int = 8) -> None:
        if buckets < 1:
            raise ValueError("é preciso ao menos um balde")
        self._buckets: list[list[tuple[str, object]]] = [[] for _ in range(buckets)]

    def put(self, key: str, value: object) -> None:
        bucket = self._buckets[hash(key) % len(self._buckets)]
        for index, (stored, _) in enumerate(bucket):
            if stored == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str) -> object:
        bucket = self._buckets[hash(key) % len(self._buckets)]
        for stored, value in bucket:
            if stored == key:
                return value
        raise KeyError(key)
