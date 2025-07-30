class UnionFind:
    def __init__(self, num_nodes: int):
        self._parents = [i for i in range(num_nodes)]
        self._rank = [1 for _ in range(num_nodes)]


    def find(self, node: int) -> int:
        """Find root node (parent) of the given node."""
        parent = self._parents[node]
        while parent != self._parents[parent]:
            self._parents[parent] = self._parents[self._parents[parent]]
            parent = self._parents[parent]
        return parent
    
    def union(self, node1: int, node2: int) -> bool:
        """Union (connect) two nodes. Return False if the two nodes are already connected."""
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            # Already in the same group.
            return False
        
        if self._rank[parent1] < self._rank[parent2]:
            self._parents[parent1] = parent2
            self._rank[parent2] += self._rank[parent1]
        else:
            self._parents[parent2] = parent1
            self._rank[parent1] += self._rank[parent2]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        unique_components = n
        for edge in edges:
            node1, node2 = edge
            if union_find.union(node1, node2):
                unique_components -= 1
        return unique_components
