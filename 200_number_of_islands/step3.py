_LAND = "1"
_SEA = "0"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse_island(start_row: int, start_col: int) -> None:
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                    continue
                if (row, col) in visited:
                    continue
                if grid[row][col] == _SEA:
                    continue
                
                visited.add((row, col))
                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))

        
        num_islands = 0
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == _LAND:
                    num_islands += 1
                    traverse_island(row, col)
        return num_islands
