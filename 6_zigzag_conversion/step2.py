class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        zigzag_pattern = [[] for _ in range(numRows)]
        step = 1
        row_index = 0
        for i, c in enumerate(s):
            zigzag_pattern[row_index].append(c)
            # In the very beginning (i == 0), it should keep going down.
            # Otherwise flipped on the table boundaries (first row or last row).
            if i != 0 and (row_index == 0 or row_index == numRows - 1):
                step *= -1 # Flip the sign of step
            row_index += step
        return ''.join(c for row in zigzag_pattern for c in row)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        def rows_generator():
            row_index = 0
            while True:
                while row_index < numRows - 1:
                    yield row_index
                    row_index += 1
                while row_index > 0:
                    yield row_index
                    row_index -= 1
        
        rows = rows_generator()
        zigzag = [[] for _ in range(numRows)]
        for c in s:
            row_index = next(rows)
            zigzag[row_index].append(c)
        return ''.join(c for row in zigzag for c in row)


class Solution3WA:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        def rows_generator():
            row_index = 0
            num_generation = 0
            while num_generation < len(s):
                while row_index < numRows - 1:
                    num_generation += 1
                    yield row_index
                    row_index += 1
                while row_index > 0:
                    num_generation += 1
                    yield row_index
                    row_index -= 1
        
        rows = rows_generator()
        zigzag = [[] for _ in range(numRows)]
        for c in s:
            for row_index in rows:
                zigzag[row_index].append(c)
        return ''.join(c for row in zigzag for c in row)


class Solution3AC:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        def rows_generator():
            row_index = 0
            num_generation = 0
            while num_generation < len(s):
                while row_index < numRows - 1:
                    num_generation += 1
                    yield row_index
                    row_index += 1
                while row_index > 0:
                    num_generation += 1
                    yield row_index
                    row_index -= 1
        
        rows = rows_generator()
        zigzag = [[] for _ in range(numRows)]
        for row_index, c in zip(rows, s):
            zigzag[row_index].append(c)
        return ''.join(c for row in zigzag for c in row)
