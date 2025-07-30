from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [inf] * (amount + 1)
        min_coins[0] = 0
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount < coin:
                    continue
                min_coins[current_amount] = min(
                    min_coins[current_amount],
                    min_coins[current_amount - coin] + 1
                )
        if min_coins[-1] == inf:
            return -1
        return min_coins[-1]
