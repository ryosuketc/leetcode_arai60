import sys


_SEA = "0"
_LAND = "1"
# The max number of rows and columns is 300 respectively, so the dfs recursion will get this deep at most.
_RECURSION_LIMIT = 300 * 300


class SolutionDfs:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse_island(row, col):
            location = (row, col)
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if location in visited:
                return
            if grid[row][col] == _SEA:
                return

            visited.add(location)
            traverse_island(row - 1, col)
            traverse_island(row + 1, col)
            traverse_island(row, col - 1)
            traverse_island(row, col + 1)

        original_recursion_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(_RECURSION_LIMIT)

        num_islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == _LAND:
                    num_islands += 1
                    traverse_island(row, col)

        sys.setrecursionlimit(original_recursion_limit)
        return num_islands


_SEA = "0"
_LAND = "1"

class SolutionIterativeDfs:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse_island(start_row, start_col):
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
                stack.append((row - 1, col))
                stack.append((row + 1, col))
                stack.append((row, col - 1))
                stack.append((row, col + 1))


        num_islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == _LAND:
                    num_islands += 1
                    traverse_island(row, col)

        return num_islands
