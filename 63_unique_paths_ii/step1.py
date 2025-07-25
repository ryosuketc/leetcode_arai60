class SolutionWA:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0] * cols for _ in range(rows)]
        # Process the first row
        for col in range(cols):
            if obstacleGrid[0][col] == 0:
                paths[0][col] = 1
        # Process the first col
        for row in range(rows):
            if obstacleGrid[row][0] == 0:
                paths[row][0] = 1
        
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    paths[row][col] = paths[row][col - 1] + paths[row - 1][col]
                else:
                    paths[row][col] = 0
        return paths[-1][-1]


class SolutionAC:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0] * cols for _ in range(rows)]
        # Process the first row
        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            paths[0][col] = 1
        # Process the first col
        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                break
            paths[row][0] = 1
        
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    paths[row][col] = paths[row][col - 1] + paths[row - 1][col]
                else:
                    paths[row][col] = 0
        return paths[-1][-1]


class SolutionAC2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0] * cols for _ in range(rows)]
        # Process the first row
        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            paths[0][col] = 1
        # Process the first col
        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                break
            paths[row][0] = 1
        
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    paths[row][col] = paths[row][col - 1] + paths[row - 1][col]
        return paths[-1][-1]


class SolutionWA2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [0] * cols
        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                break
            paths[col] = 1
        for row in range(1, rows):
            print(paths)
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    paths[col] = paths[col - 1] + paths[col]
        return paths[-1]
