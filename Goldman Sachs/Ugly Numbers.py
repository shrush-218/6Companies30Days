'''
	Goldman Sachs Question 5: Ugly Numbers

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. 
By convention, 1 is included. Write a program to find Nth Ugly Number.

'''

#User function Template for python3
class Solution:
	def getNthUglyNo(self,n):
		l = [1]
		p2, p3, p5 = 0, 0, 0
		for i in range(1,n):
			# get the next number
			next_num = min(2*l[p2], min(3*l[p3], 5*l[p5]))
			l.append(next_num)
			# increase pointer for which the number matches [see above explanation]
			if next_num == 2 * l[p2]:
				p2 += 1
			if next_num == 3 * l[p3]:
				p3 += 1
			if next_num == 5 * l[p5]:
				p5 += 1
		return l[n-1]
			

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		ob = Solution()
		ans = ob.getNthUglyNo(n);
		print(ans)
		tc -= 1

# } Driver Code Ends