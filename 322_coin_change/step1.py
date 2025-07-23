# Memory Limite Exceeded

from math import inf


class Solution1MLE:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = inf

        @cache
        def coin_change_helper(amount, num_coins):
            if amount == 0:
                nonlocal min_coins
                min_coins = min(min_coins, num_coins)
                return
            for coin in coins:
                if amount < coin:
                    continue
                coin_change_helper(amount - coin, num_coins + 1)
        
        coin_change_helper(amount, 0)
        if min_coins == inf:
            return -1
        return min_coins
