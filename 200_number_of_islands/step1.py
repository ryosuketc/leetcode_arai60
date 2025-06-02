class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse_island(row, col, visited):
            location = (row, col)
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if location in visited:
                return
            if grid[row][col] == "0":
                return

            visited.add(location)
            traverse_island(row - 1, col, visited)
            traverse_island(row + 1, col, visited)
            traverse_island(row, col - 1, visited)
            traverse_island(row, col + 1, visited)


        num_islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    num_islands += 1
                    traverse_island(row, col, visited)
        return num_islands
