import heapq
from collections import deque


def breadth_first(graph: dict[str, list[str]], start: str) -> list[str]:
    """Visita o grafo em largura. Cada aresta entra uma vez: O(V + A)."""
    if start not in graph:
        return []
    seen = {start}
    order = [start]
    queue: deque[str] = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                order.append(neighbor)
                queue.append(neighbor)
    return order


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    """Menor distância a partir de start. Pesos não negativos. Tempo O((V + A) log V)."""
    distances = {start: 0}
    pending = [(0, start)]
    while pending:
        distance, node = heapq.heappop(pending)
        if distance != distances.get(node):
            continue
        for neighbor, weight in graph.get(node, []):
            if weight < 0:
                raise ValueError("Dijkstra exige pesos não negativos")
            candidate = distance + weight
            if candidate < distances.get(neighbor, 10**18):
                distances[neighbor] = candidate
                heapq.heappush(pending, (candidate, neighbor))
    return distances
