'''
	Goldman Sachs Question 12: Squares in Chessboard

Find total number of Squares in a N*N cheesboard.

'''

#User function Template for python3

class Solution:
    def squaresInChessBoard(self, N):
        if N==1:
             return N
        ans=N*N
        N-=1
        while N>1:
            ans+=N*N
            N-=1
        
        return ans+1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))
# } Driver Code Ends