'''
	Intuit Question 13: Minimum Swaps to Arrange a Binary Grid

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them. A grid is said 
to be valid if all the cells above the main diagonal are zeros. Return the minimum number of steps needed to make 
the grid valid, or -1 if the grid cannot be valid. 
The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

'''
class Solution:
    def minSwaps(self, grid):
        swaps = 0
        zeroesNeeded = len(grid)-1 
        start = 1
        
        for i in range(len(grid)):
            temp = i
            while temp < len(grid) and grid[temp][start:] != [0]*zeroesNeeded:
                temp += 1
                
            if temp >= len(grid):
                return -1
            
            start += 1
            zeroesNeeded -= 1
            
            while temp > i:
                grid[temp], grid[temp-1] = grid[temp-1], grid[temp]
                temp -= 1
                swaps += 1
                
        return swaps
        