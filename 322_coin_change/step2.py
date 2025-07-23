
#WA
from math import inf, isinf


class Solution1WA:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def coin_change_helper(amount):
            print(amount)
            if amount == 0:
                return 0
            min_coins = inf
            for coin in coins:
                if amount < coin:
                    continue
                min_coins = min(min_coins, coin_change_helper(amount - coin) + 1)
            print(f"amount={amount}, min_coins={min_coins}")
            if isinf(min_coins):
                return -1
            return min_coins
        
        return coin_change_helper(amount)

# WA
from math import inf, isinf


class Solution2WA:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def coin_change_helper(amount) -> int | None:
            if amount < 0:
                return None
            if amount == 0:
                return 0
            min_coins = inf
            for coin in coins:
                min_coins_with_coin = coin_change_helper(amount - coin)
                if min_coins_with_coin is not None:
                    min_coins = min(min_coins, min_coins_with_coin + 1)
                print(f"amount={amount}, min_coins={min_coins}")
            if isinf(min_coins):
                return -1
            return min_coins
        
        return coin_change_helper(amount)



# AC: Recursion
from math import inf, isinf


class Solution3AC:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def coin_change_helper(amount) -> int | None:
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            min_coins = inf
            for coin in coins:
                min_coins_with_coin = coin_change_helper(amount - coin)
                if min_coins_with_coin != -1:
                    min_coins = min(min_coins, min_coins_with_coin + 1)
            if isinf(min_coins):
                return -1
            return min_coins
        
        return coin_change_helper(amount)


# AC: DP
from math import inf


class Solution4AC:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [inf] * (amount + 1)
        min_coins[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
        if isinf(min_coins[-1]):
            return -1
        return min_coins[-1]
