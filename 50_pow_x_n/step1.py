class Solution1WA:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        result = x
        exponent = n
        while exponent != 1:
            result *= result
            exponent //= 2
        if n % 2 == 1:
            result *= x
        return result


class Solution2AC:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1.0 / x
        result = 1
        exponent = n
        base = x
        while exponent != 0:
            if exponent % 2 == 1:
                result *= base
                exponent -= 1
            base *= base
            exponent //= 2

        return result
