'''
	Adobe Question 12: Leaders in an array 

Given an array A of positive integers. Your task is to find the leaders in 
the array. An element of array is leader if it is greater than or equal to 
all the elements to its right side. The rightmost element is always a leader. 

'''
class Solution:
    def leaders(self, A, N):
        res = []
        max_value = -999
        for value in reversed(A):
            if value>=max_value:
                max_value=value
                res.append(max_value)
                
        return res[::-1]

import math    
def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        A=obj.leaders(A,N)
        for i in A:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
