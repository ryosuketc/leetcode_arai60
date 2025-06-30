class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        total_ways = [0] * n
        total_ways[0] = k
        total_ways[1] = k * k
        for i in range(2, n):
            total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])
        return total_ways[n - 1]
        # -1 でもいけるが、上の方が可読性が高い (0-index で n 番目の値にアクセスしている)
        # return total_ways[-1]
