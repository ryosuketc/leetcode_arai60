# memory limit exceeded
class SolutionMLE:
    def kthGrammar(self, n: int, k: int) -> int:
        row = '0'
        for i in range(n):
            next_row = []
            for char in row:
                if char == '0':
                    next_row.append('01')
                elif char == '1':
                    next_row.append('10')
            row = ''.join(next_row)
        return int(''.join(row)[k - 1])


