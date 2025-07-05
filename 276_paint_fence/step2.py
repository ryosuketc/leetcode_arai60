class SolutionManualMemo:
    def numWays(self, n: int, k: int) -> int:
        memo = {}

        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in memo:
                return memo[i]
            
            memo[i] = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
            return memo[i]

        return total_ways(n)


from functools import lru_cache


class SolutionLruCache:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        return total_ways(n)


class SolutionBottomUp:
    def numWays(self, n: int, k: int) -> int:
        total_ways = [0, k, k * k]
        for i in range(3, n + 1):
            num_ways = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])
            total_ways.append(num_ways)
        return total_ways[n]


class SolutionBottomUpConstantSpace:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        two_posts_back = k
        one_post_back = k * k
        for i in range(3, n + 1):
            post = (k - 1) * (one_post_back + two_posts_back)
            two_posts_back = one_post_back
            one_post_back = post
        return one_post_back


# デコレータ自分で書いてみる
def memo(func):
    memo = {}
    def wrapper(*args, **kwargs):
        key = tuple(args) + tuple(kwargs.items())
        if key in memo:
            return memo[key]
        memo[key] = func(*args, **kwargs)
        return memo[key]
    return wrapper


class SolutionMyDecorator:
    def numWays(self, n: int, k: int) -> int:
        @memo
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        return total_ways(n)


class SolutionMyDecoratorTLE:
    def numWays(self, n: int, k: int) -> int:
        @memo
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        return total_ways(n)


class SolutionMyDecoratorNoSyntaxSugar:
    def numWays(self, n: int, k: int) -> int:
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

        total_ways = memo(total_ways)
        return total_ways(n)
