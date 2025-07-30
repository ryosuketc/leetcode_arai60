INT_MAX = (1 << 31) - 1
INT_MIN = -INT_MAX - 1

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
        
        # Process the rest.
        result = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            digit = ord(s[i]) - ord('0')
            is_overflow = result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10)
            if is_overflow:
                if sign == -1:
                    return INT_MIN
                return INT_MAX
            result = result * 10 + digit
            i += 1
        return sign * result
