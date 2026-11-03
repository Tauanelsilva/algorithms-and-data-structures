import pytest

from algorithms.graphs import breadth_first, dijkstra
from algorithms.search import binary_search
from algorithms.sorting import merge_sort
from algorithms.structures import HashMap, Queue, Stack


def test_merge_sort_keeps_original_and_orders():
    original = [4, 1, 3, 2, 2]
    assert merge_sort(original) == [1, 2, 2, 3, 4]
    assert original == [4, 1, 3, 2, 2]
    assert merge_sort([]) == []


def test_binary_search():
    values = [1, 3, 5, 7, 9]
    assert binary_search(values, 7) == 3
    assert binary_search(values, 2) == -1
    assert binary_search([], 1) == -1


def test_breadth_first_avoids_cycles():
    graph = {"a": ["b", "c"], "b": ["a"], "c": ["d"], "d": []}
    assert breadth_first(graph, "a") == ["a", "b", "c", "d"]
    assert breadth_first(graph, "z") == []


def test_dijkstra():
    graph = {
        "a": [("b", 1), ("c", 4)],
        "b": [("c", 1)],
        "c": [],
    }
    assert dijkstra(graph, "a") == {"a": 0, "b": 1, "c": 2}


def test_dijkstra_rejects_negative_weight():
    with pytest.raises(ValueError):
        dijkstra({"a": [("b", -1)], "b": []}, "a")


def test_stack_queue_and_hash():
    stack = Stack()
    stack.push("primeiro")
    stack.push("segundo")
    assert stack.pop() == "segundo"

    queue = Queue()
    queue.enqueue("primeiro")
    queue.enqueue("segundo")
    assert queue.dequeue() == "primeiro"

    table = HashMap(buckets=2)
    table.put("a", 1)
    table.put("b", 2)
    table.put("a", 3)
    assert table.get("a") == 3
    assert table.get("b") == 2
    with pytest.raises(KeyError):
        table.get("ausente")
