class Solution:
    def numWays(self, n: int, k: int) -> int:
        total_ways = [0, k, k * k]
        for i in range(3, n + 1):
            num_ways = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])
            total_ways.append(num_ways)
        return total_ways[n]
