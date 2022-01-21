'''
	Adobe Question 6: Generate Parentheses 

Given an integer N representing the number of pairs of parentheses, 
the task is to generate all combinations of well-formed(balanced) 
parentheses.

'''

class Solution:
    def Solve(self,limit,curr,result,s,count):
        if curr==limit:
            if count==0:
                result.append(s)
        if curr<limit:
            self.Solve(limit, curr+1,result,s+'(',count+1)
        if count>0:
            self.Solve(limit, curr,result,s+')',count-1)
            
    def AllParenthesis(self,n):
        result=[]
        self.Solve(n,0,result,'',0)
        return result
               
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
       