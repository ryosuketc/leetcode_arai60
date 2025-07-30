class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        going_down = True
        row_index = 0
        for i, c in enumerate(s):
            zigzag[row_index].append(c)
            if i != 0 and row_index == 0:
                going_down = True
            elif row_index == numRows - 1:
                going_down = False
            if going_down:
                row_index += 1
            else:
                row_index -= 1
        return ''.join(c for row in zigzag for c in row)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        going_down = True
        row_index = 0
        for i, c in enumerate(s):
            zigzag[row_index].append(c)
            if i != 0 and row_index == 0 or row_index == numRows - 1:
                going_down = not going_down
            if going_down:
                row_index += 1
            else:
                row_index -= 1
        return ''.join(c for row in zigzag for c in row)
