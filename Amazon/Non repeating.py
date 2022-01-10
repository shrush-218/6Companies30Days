'''
	Amazon Question 7:  First non-repeating character in a stream 

Given an input stream of A of n characters consisting only of lower case 
alphabets. The task is to find the first non repeating character, each time 
a character is inserted to the stream. If there is no such character then 
append '#' to the answer.


'''

#User function Template for python3
class Solution:
	def FirstNonRepeating(self, A):
		frequency=[0]*26
		queue=[]
		ans=''
		for i in range(len(A)):
			c=A[i]
			frequency[ord(c)-97]+=1
			if frequency[ord(c)-97]==1:
				queue.append(c)
			else:
				while queue and frequency[ord(queue[0])-97]>1:
					queue.pop(0)
			if queue:
				ans+=queue[0]
			else:
				ans+='#'
		return ans
			
			
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends