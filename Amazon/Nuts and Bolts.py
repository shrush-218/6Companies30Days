'''
	Amazon Question 10:  Nuts and Bolts Problem 

Given a set of N nuts of different sizes and N bolts of different 
sizes. There is a one-one mapping between nuts and bolts. Match nuts 
and bolts efficiently.
Comparison of a nut to another nut or a bolt to another bolt is not 
allowed. It means nut can only be compared with bolt and bolt can only 
be compared with nut to see which one is bigger/smaller.
The elements should follow the following order ! # $ % & * @ ^ ~ .
'''

#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
		lst = ['!','#','$','%','&','*','@','^','~']
		res = []
		for el in lst:
			if el in nuts:
				res.append(el)
		for i in range(n):
			nuts[i],bolts[i] = res[i],res[i]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		nuts = list(map(str, input().strip().split()))
		bolts = list(map(str, input().strip().split()))
		ob = Solution()
		ob.matchPairs(nuts, bolts, n)
		for x in nuts:
			print(x, end=" ")
		print()
		for x in bolts:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends