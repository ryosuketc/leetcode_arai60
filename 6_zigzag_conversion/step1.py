class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        # Compressed table...
        # Rather than this...
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I
        # Create this instead:
        # P I N
        # A L S  I G
        # Y A H R
        # P I
        if numRows <= 1:
            return s
        zigzag_pattern = [[] for _ in range(numRows)]
        # Initially not going down as it will be immediately flipped in s[0].
        going_down = False
        row_index = 0
        for c in s:
            zigzag_pattern[row_index].append(c)
            if row_index == 0 or row_index == (numRows - 1):
                going_down = not going_down
            if going_down:
                row_index += 1
            else: # Going up
                row_index -= 1
        return ''.join(c for row in zigzag_pattern for c in row)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        zigzag_pattern = [[] for _ in range(numRows)]
        going_down = True
        row_index = 0
        for i, c in enumerate(s):
            zigzag_pattern[row_index].append(c)
            # In the very beginning (i == 0), it should keep going down.
            # Otherwise flipped on the table boundaries (first row or last row).
            if i != 0 and (row_index == 0 or row_index == numRows - 1):
                going_down = not going_down
            if going_down:
                row_index += 1
            else: # Going up
                row_index -= 1
        return ''.join(c for row in zigzag_pattern for c in row)
