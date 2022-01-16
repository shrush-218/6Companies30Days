'''
	Microsoft Question 1: Minimum Sum Partition

Given an integer array arr of size N, the task is to divide it into 
two sets S1 and S2 such that the absolute difference between their 
sums is minimum and find the minimum difference.

'''

# User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		total_sum = sum(arr)
		memo = [[False for j in range((total_sum//2)+1)]for i in range(n+1)]
		for i in range(len(memo)):
			memo[i][0] = True
		for i in range(1, len(memo)):
			for j in range(1,len(memo[0])):
				if arr[i-1] <= j:
					memo[i][j] = memo[i-1][j-arr[i-1]] or memo[i-1][j]
				else:
					memo[i][j] = memo[i-1][j]
					
		min_diff = float('inf')
		for i in range(len(memo[0])-1, -1, -1):
			if memo[-1][i]:
				min_diff = min(min_diff, abs(total_sum-(2*i)))
				return min_diff
					
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends