class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1.0 / x
        base = x
        exponent = n
        result = 1
        while exponent != 0:
            if exponent % 2 == 1:
                result *= base
                exponent -= 1
            base *= base
            exponent //= 2
        return result
