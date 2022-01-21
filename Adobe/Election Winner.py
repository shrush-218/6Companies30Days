'''
	Adobe Question 10: Winner of an election 

Given an array of names (consisting of lowercase characters) of candidates in 
an election. A candidate name in array represents a vote casted to the candidate. 
Print the name of candidate that received Max votes. If there is tie, print 
lexicographically smaller name.

'''
from collections import Counter
class Solution:
    
    def winner(self,arr,n):
        ay=Counter(arr)
        b=sorted(ay.items(), key=lambda item: (-item[1], item[0]))
        return (b[0])

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])