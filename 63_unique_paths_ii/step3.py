OBSTACLE = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0] * cols for _ in range(rows)]
        # First row
        for col in range(cols):
            if obstacleGrid[0][col] == OBSTACLE:
                break
            paths[0][col] = 1
        # First col
        for row in range(rows):
            if obstacleGrid[row][0] == OBSTACLE:
                break
            paths[row][0] = 1
        
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == OBSTACLE:
                    continue
                paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[-1][-1]
                
