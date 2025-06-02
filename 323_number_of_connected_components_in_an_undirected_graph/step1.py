# Wrong Answer
from collections import defaultdict


class SolutionWA:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def make_graph():
            # Represented as a adjacency list.
            graph = defaultdict(list)
            for edge in edges:
                node1, node2 = edge
                graph[node1].append(node2)
                graph[node2].append(node1)
            return graph
        

        visited = set()
        unique_components = 0
        graph = make_graph()
        for source in range(n):
            if source not in visited:
                unique_components += 1
                visited.add(source)
            for destination in graph[source]:
                if destination not in visited:
                    visited.add(destination)

        return unique_components


# Accepted
from collections import defaultdict


class SolutionAccepted:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def make_graph():
            # Represented as a adjacency list.
            graph = defaultdict(list)
            for edge in edges:
                node1, node2 = edge
                graph[node1].append(node2)
                graph[node2].append(node1)
            return graph
        
        def visit(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for connected_node in graph[node]:
                visit(connected_node)
        

        visited = set()
        unique_components = 0
        graph = make_graph()
        for source in range(n):
            if source not in visited:
                unique_components += 1
                visit(source)

        return unique_components
