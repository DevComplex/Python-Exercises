import collections

moves = [[1, 0], [0, 1], [-1, 0], [0, - 1]]

def countZeros(grid, i, j):
    zeroes = 0

    for move in moves:
        nextRow = i + move[0]
        nextCol = j + move[1]

        if nextCol < 0 or nextRow < 0 or nextCol == len(grid[0]) or nextRow == len(grid):
            zeroes += 1
        elif grid[nextRow][nextCol] == 0:
            zeroes += 1

    return zeroes 

def islandPerimeter(grid):
    perimeter = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                queue = collections.deque([(i, j)])
                visited.add((i, j))

                while len(queue > 0):
                    row, col = queue.popleft()
                    perimeter += countZeros(grid, row, col)

                    for move in moves:
                        nextRow = i + move[0]
                        nextCol = j + move[1]

                        if nextCol < 0 or nextRow < 0 or nextCol == len(grid[0]) or nextRow == len(grid):
                            zeroes += 1
                        elif grid[nextRow][nextCol] == 0:
                            zeroes += 1
                        elif grid[nextRow][nextCol] == 1 and (nextRow, nextCol) not in visited:
                            visited.add((nextRow, nextCol))

                return perimeter


    return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(islandPerimeter(grid))