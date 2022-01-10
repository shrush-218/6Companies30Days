'''
	Amazon Question 8:  Count Ways to N-th stair

There are N stairs, and a person standing at the bottom wants to reach 
the top. The person can climb either 1 stair or 2 stairs at a time. Count 
the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n=4 {1 2 1},{2 1 1},{1 1 2} are 
considered same.
'''


#User function Template for python3

class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        
        return (m//2)+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends