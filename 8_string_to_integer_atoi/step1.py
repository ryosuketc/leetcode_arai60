MIN_INT = -2**31
MAX_INT = 2**31 - 1


class Solution1:
    def myAtoi(self, s: str) -> int:
        sign = 1 # Positive by default
        i = 0
        # Skip leading whitespaces.
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        # Skip leading zeros.
        while i < len(s) and s[i] == '0':
            i += 1
        while i < len(s) and s[i].isdigit():
            result += int(s[i])
            result *= 10
            i += 1

        result //= 10
        if sign < 0:
            return max(-result, MIN_INT)
        return min(result, MAX_INT)


MIN_INT = -2**31
MAX_INT = 2**31 - 1


class Solution2:
    def myAtoi(self, s: str) -> int:
        def preprocess() -> tuple[int, int]:
            """ Preprocess s to get the first index to furthrer process and a sign.
            
            Returns:
                A tuple of
                1. the index after leading whitespaces, sign and leading zeros and
                2. sign (1 == positive and -1 == negative).
            """
            i = 0
            # Skip leading whitespaces.
            while i < len(s) and s[i] == ' ':
                i += 1
            sign = 1
            if i < len(s) and s[i] in '+-':
                if s[i] == '-':
                    sign = -1
                i += 1
            # Skip leading zeros.
            while i < len(s) and s[i] == '0':
                i += 1
            return i, sign
        
        index, sign = preprocess()
        result = 0
        for i in range(index, len(s)):
            if not s[i].isdigit():
                break
            result += int(s[i])
            result *= 10
        result //= 10

        if sign < 0:
            return max(-result, MIN_INT)
        return min(result, MAX_INT)


MIN_INT = -2**31
MAX_INT = 2**31 - 1


class Solution3:
    def myAtoi(self, s: str) -> int:
        def preprocess() -> tuple[int, int]:
            """ Preprocess s to get the first index to furthrer process and a sign.
            
            Returns:
                A tuple of
                1. the index after leading whitespaces, sign and leading zeros and
                2. sign (1 == positive and -1 == negative).
            """
        result = 0
        # Remove leading whilespaces.
        preprocessed_s = s.lstrip()
        if not preprocessed_s:
            return result
        sign = 1
        if preprocessed_s[0] in '-+':
            if preprocessed_s[0] == '-':
                sign = -1
            preprocessed_s = preprocessed_s[1:]
        # Remove leading zeros.
        preprocessed_s = preprocessed_s.lstrip('0')

        result = 0
        for i in range(len(preprocessed_s)):
            if not preprocessed_s[i].isdigit():
                break
            result += int(preprocessed_s[i])
            result *= 10
        result //= 10

        if sign < 0:
            return max(-result, MIN_INT)
        return min(result, MAX_INT)
