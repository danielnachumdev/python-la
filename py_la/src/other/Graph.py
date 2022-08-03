from __future__ import annotations
from typing import Any, Tuple


class DirectedGraph:
    def __init__(self, verticies: set[Any], edges: set[Tuple[Any, Any]], weights: dict[Tuple[Any, Any], float] = None) -> None:
        self.verticies = verticies
        self.edges = edges
        self.weights = weights

    def __contains__(self, edge: Tuple[Any, Any]) -> bool:
        return edge in self.edges

    def weight(self, edge: Tuple[Any, Any]) -> float:
        if not edge in self:
            raise ValueError("Edge not in graph")
        if not self.weights:
            raise ValueError("Graph has no weights")
        return self.weights[edge]


class UnderictedGraph(DirectedGraph):
    def __init__(self, verticies: set[Any], edges: set[Tuple[Any, Any]], weights: dict[Tuple[Any, Any], float] = None) -> None:
        super().__init__(
            verticies,
            edges + set([(edge[1], edge[0])for edge in edges]),
            # weights+set([(edge[1], edge[0]) for edge in weights.keys()]),
        )
