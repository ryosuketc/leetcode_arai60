class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -n

        powered = 1
        cumulated = x
        exponent = n
        # e.g. 3^14 = 3^(2^3) * 3^(2^2) * 3^(2^1)
        # bin(14) == 0b1110
        
        # e.g. 3^5 = * 3^(2^2) * 3^(2^0)
        # bin(14) == 0b101
        # powered=1, cumulated=3.0, exponent=5
        # powered=3.0, cumulated=9.0, exponent=2
        # powered=3.0, cumulated=81.0, exponent=1
        while exponent > 0:
            print(f'powered={powered}, cumulated={cumulated}, exponent={exponent}')
            if exponent & 1:
                powered *= cumulated
            exponent >>= 1
            cumulated *= cumulated
        return powered
