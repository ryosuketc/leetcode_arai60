WATER = 0


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_area_of_island(start_row: int, start_col: int) -> int:
            area = 0
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                    continue
                if (row, col) in visited:
                    continue
                if grid[row][col] == WATER:
                    continue
                
                area += 1
                visited.add((row, col))
                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))
            return area

        max_area = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, get_area_of_island(row, col))
        return max_area
