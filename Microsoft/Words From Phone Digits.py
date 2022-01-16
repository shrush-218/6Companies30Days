'''
	Microsoft Question 6: Possible words from phone digits

Given a keypad as shown in the diagram, and an N digit number which is represented 
by array a[ ], the task is to list all words which are possible by pressing these 
numbers.

'''
class Solution:
    def possibleWords(self,a,N):
        mp = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        def solve(i,cur,result):
            if i==N:
                result.append("".join(cur))
                return
            for ch in mp[a[i]]:
                cur.append(ch)
                solve(i+1,cur,result)
                cur.pop()
        result = []
        solve(0,[],result)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends