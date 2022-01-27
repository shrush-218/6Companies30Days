'''
	Intuit Question 9: Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's 
left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. The island is partitioned into a grid of square 
cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate 
(r, c). The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the 
neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the 
ocean. Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both 
the Pacific and Atlantic oceans.
    
'''
import collections
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        
        #get adjacent nodes, i.e. there is an edge
        def adjacent(r, c):
            for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= i < R and 0 <= j < C and matrix[r][c] <= matrix[i][j]:
                    yield (i, j)
        
        #Atlantic BFS
        que = collections.deque([])
        atlantic = [[0]*C for _ in range(R)]
        for r in range(R):
            que.append((r, C-1))
        for c in range(C-1):
            que.append((R-1, c))
        while que:
            r, c = que.popleft()
            atlantic[r][c] = 1
            for i, j in adjacent(r, c):
                if not atlantic[i][j]:
                    que.append((i, j))
        
        #Pacific BFS
        que = collections.deque([])
        pacific = [[0]*C for _ in range(R)]
        for r in range(R):
            que.append((r, 0))
        for c in range(1, C):
            que.append((0, c))
        while que:
            r, c = que.popleft()
            pacific[r][c] = 1
            for i, j in adjacent(r, c):
                if not pacific[i][j]:
                    que.append((i, j))
        
        #Find all nodes that can access both Oceans
        ans = []
        for r in range(R):
            for c in range(C):
                if atlantic[r][c] and pacific[r][c]:
                    ans.append([r, c])
        return ans
