'''
    Walmart Question 4: Number Of Unique Paths

Given a A X B matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of 
the matrix from the initial position. 
Note: Possible moves can be either down or right at any point in time, i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j].

'''
 
class Solution:
    def NumberOfPaths(self, a, b):
        mat=[[0]*b for j in range(a)]
        for i in range(a):
            for j in range(b):
                if(i==0 or j==0):
                    mat[i][j]=1
                else:
                    mat[i][j]=(mat[i-1][j]+mat[i][j-1])
        return mat[a-1][b-1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))
