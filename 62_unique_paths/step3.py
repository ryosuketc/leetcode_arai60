class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        paths = [1] * cols
        for _ in range(1, rows):
            for col in range(1, cols):
                paths[col] = paths[col] + paths[col - 1]
        return paths[-1]
