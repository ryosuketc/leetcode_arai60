MAX_INT = (1 << 31) - 1 # 2147483647
MIN_INT = -MAX_INT - 1 # -2147483648


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        # Skip leading whitespaces.
        while i < len(s) and s[i] == ' ':
            i += 1
        # Get sign
        sign = 1
        if i < len(s) and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        # Skip leading zeros.
        while i < len(s) and s[i] == '0':
            i += 1
        
        result = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            digit = ord(s[i]) - ord('0')
            is_over_limit = result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > MAX_INT % 10)
            if is_over_limit:
                if sign == -1:
                    return MIN_INT
                return MAX_INT
            result = result * 10 + digit
            i += 1
        return sign * result
