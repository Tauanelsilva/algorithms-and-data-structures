def binary_search(values: list[int], target: int) -> int:
    """Devolve o índice de target em uma lista já ordenada, ou -1. Tempo O(log n)."""
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
