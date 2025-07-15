class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        paths = [[1] * cols for _ in range(rows)]
        for row in range(1, rows):
            for col in range(1, cols):
                paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[-1][-1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        previous_paths = [1] * cols
        paths = [1] * cols
        for row in range(1, rows):
            for col in range(1, cols):
                print(col)
                paths[col] = previous_paths[col] + paths[col - 1]
            previous_paths, paths = paths, [1] * cols
        return previous_paths[-1]
