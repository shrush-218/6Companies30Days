'''
	Amazon Question 13:  Rotten Oranges

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten 
orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh 
orange. If this is impossible, return -1.

'''
class Solution:
    def orangesRotting(self, grid):
        
        m, n = len(grid), len(grid[0])
        counter = 0
        
        from collections import deque
        q = deque()
        start = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    start.append((i,j))
        if start:
            q.append(start)
                    
        while q:
            search = q.popleft()
            perform_rotten = 0
            search_ = []
            for (i, j) in search:
                for i_, j_, in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (0 <= i_ <= m - 1) and (0 <= j_ <= n - 1) and (grid[i_][j_] == 1):
                        perform_rotten = 1
                        grid[i_][j_] = 2
                        search_.append((i_, j_))
            if perform_rotten:
                counter += 1
            if search_:
                q.append(search_)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return counter
        