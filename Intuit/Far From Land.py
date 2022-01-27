'''
	Intuit Question 14: As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water 
cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water 
exists in the grid, return -1. The distance used in this problem is the Manhattan distance: the distance between 
two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

'''
from collections import deque
class Solution:
    def maxDistance(self, grid):
        m,n = len(grid), len(grid[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level-1
        