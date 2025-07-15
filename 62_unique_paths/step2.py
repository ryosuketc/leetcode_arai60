from math import factorial


class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        return factorial(rows + cols - 2) // factorial(rows - 1) // factorial(cols - 1)


from functools import cache


class SolutionRecursive:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class SolutionDP:
    def uniquePaths(self, m: int, n: int) -> int:
        height = m
        width = n
        paths = [1] * width
        for _ in range(1, height):
            for position in range(1, width):
                # 2d DP でいうと
                # paths[position - 1]: 前の列, paths[position]: 前の行
                paths[position] = paths[position] + paths[position - 1]
        return paths[-1]
